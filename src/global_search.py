import os

from dotenv import load_dotenv
import pandas as pd
import tiktoken

from graphrag.query.indexer_adapters import read_indexer_entities, read_indexer_reports
from graphrag.query.llm.oai.chat_openai import ChatOpenAI
from graphrag.query.llm.oai.typing import OpenaiApiType
from graphrag.query.structured_search.global_search.community_context import (
    GlobalCommunityContext,
)
from graphrag.query.structured_search.global_search.search import GlobalSearch

load_dotenv()
api_key = os.getenv("api_key")
llm_model = os.getenv("llm_model")

llm = ChatOpenAI(
    api_key=api_key,
    model=llm_model,
    api_type=OpenaiApiType.OpenAI,  # OpenaiApiType.OpenAI or OpenaiApiType.AzureOpenAI
    max_retries=20,
)

token_encoder = tiktoken.get_encoding("cl100k_base")
# Prompt the user for input
valid_choices = {'MDS': 'minerals_domain_schema',
                 'EMDS': 'expanded_minerals_domain_schema',
                 'AS': 'auto_generated_schema',
                 'SL': 'schema_less'}

user_choice = input("Enter your schema choice (MDS, EMDS, AS, SL): ").strip().upper()
while user_choice not in valid_choices:
    print("Invalid choice. Please select from MDS, EMDS, AS, SL.")
    user_choice = input("Enter your choice (MDS, EMDS, AS, SL): ").strip().upper()

# Determine the base path based on user input
base_path = os.path.dirname(os.path.abspath(__file__))
schema_directory = valid_choices[user_choice]
output_dir = os.path.join(base_path, schema_directory, 'output')

# Search for the 'artifacts' directory
INPUT_DIR = None
for root, dirs, files in os.walk(output_dir):
    if 'artifacts' in dirs:
        INPUT_DIR = os.path.join(root, 'artifacts')
        break

# Display the result
if INPUT_DIR:
    print(f"Artifacts directory found: {INPUT_DIR}")
else:
    print("No artifacts directory found.")

COMMUNITY_REPORT_TABLE = "create_final_community_reports"
ENTITY_TABLE = "create_final_nodes"
ENTITY_EMBEDDING_TABLE = "create_final_entities"

# community level in the Leiden community hierarchy from which we will load the community reports
# higher value means we use reports from more fine-grained communities (at the cost of higher computation cost)
COMMUNITY_LEVEL = 2

entity_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_TABLE}.parquet")
report_df = pd.read_parquet(f"{INPUT_DIR}/{COMMUNITY_REPORT_TABLE}.parquet")
entity_embedding_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_EMBEDDING_TABLE}.parquet")

reports = read_indexer_reports(report_df, entity_df, COMMUNITY_LEVEL)
entities = read_indexer_entities(entity_df, entity_embedding_df, COMMUNITY_LEVEL)
# print(f"Report records: {len(report_df)}")
report_df.head()

context_builder = GlobalCommunityContext(
    community_reports=reports,
    entities=entities,  # default to None if you don't want to use community weights for ranking
    token_encoder=token_encoder,
)

context_builder_params = {
    "use_community_summary": False,  # False means using full community reports. True means using community short summaries.
    "shuffle_data": True,
    "include_community_rank": True,
    "min_community_rank": 0,
    "community_rank_name": "rank",
    "include_community_weight": True,
    "community_weight_name": "occurrence weight",
    "normalize_community_weight": True,
    "max_tokens": 12_000,  # change this based on the token limit you have on your model (if you are using a model with 8k limit, a good setting could be 5000)
    "context_name": "Reports",
}

map_llm_params = {
    "max_tokens": 1000,
    "temperature": 0.0,
    "response_format": {"type": "json_object"},
}

reduce_llm_params = {
    "max_tokens": 2000,  # change this based on the token limit you have on your model (if you are using a model with 8k limit, a good setting could be 1000-1500)
    "temperature": 0.0,
}

search_engine = GlobalSearch(
    llm=llm,
    context_builder=context_builder,
    token_encoder=token_encoder,
    max_data_tokens=12_000,  # change this based on the token limit you have on your model (if you are using a model with 8k limit, a good setting could be 5000)
    map_llm_params=map_llm_params,
    reduce_llm_params=reduce_llm_params,
    allow_general_knowledge=False,  # set this to True will add instruction to encourage the LLM to incorporate general knowledge in the response, which may increase hallucinations, but could be useful in some use cases.
    json_mode=True,  # set this to False if your LLM model does not support JSON mode.
    context_builder_params=context_builder_params,
    concurrent_coroutines=32,
    response_type="multiple paragraphs",  # free form text describing the response type and format, can be anything, e.g. prioritized list, single paragraph, multiple paragraphs, multiple-page report
)

def answer_query(chat, query, debug=False):
    result = search_engine.search(query)

    result_row = {
        "query": query,
        "response": result.response,
        "llm_calls": result.llm_calls,
        "prompt_tokens": result.prompt_tokens,
        #"output_tokens": result.output_tokens,
        "reports": result.context_data.get("reports", pd.DataFrame()).head().to_json(),
    }

    return result_row


if __name__ == "__main__":
    questions = [
            "Identify which MRIWA reports reference MERIWA or MRIWA.",
            "Extract all references to MERIWA and MRIWA from the MRIWA reports.",
            "Identify any references to nickel or Ni in the MRIWA reports.",
            "Which elements are considered in the MRIWA reports?",
            "Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with in any capacity (including being listed in references)?",
            "Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a researcher?",
            "Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a sponsor?",
            "Which MRIWA report is related to the East Kimberley region?",
            "Which regions of Western Australia are referenced in the MRIWA reports?",
            "Which MRIWA report author has been involved in more than one report/project?",
            "What is the average number of references in each MRIWA report?",
            "Which MRIWA reports relate to leaching?",
            "Which MRIWA reports relate to exploration?",
            "Which MRIWA reports relate to mining extraction?",
            "Which MRIWA reports relate to mineral processing?",                
    ]

    results_list = []
    for query in questions:

        print("Query:\n")
        print(query)
        print("\n")

        result_row = answer_query([], query, debug=False)

        results_list.append(result_row)

        print("Response:\n")
        print(result_row["response"])
        print("\n")

    df_results = pd.DataFrame(results_list)
    csv_filename = user_choice + "_global_results.csv"
    df_results.to_csv(csv_filename, index=False)
    print("Saved results to " + csv_filename)