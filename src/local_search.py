import os

import pandas as pd
import tiktoken

from graphrag.query.context_builder.entity_extraction import EntityVectorStoreKey
from graphrag.query.indexer_adapters import (
    read_indexer_entities,
    read_indexer_relationships,
    read_indexer_reports,
    read_indexer_text_units,
)
from graphrag.query.input.loaders.dfs import (
    store_entity_semantic_embeddings,
)
from graphrag.query.llm.oai.chat_openai import ChatOpenAI
from graphrag.query.llm.oai.embedding import OpenAIEmbedding
from graphrag.query.llm.oai.typing import OpenaiApiType
from graphrag.query.structured_search.local_search.mixed_context import (
    LocalSearchMixedContext,
)
from graphrag.query.structured_search.local_search.search import LocalSearch
from graphrag.vector_stores.lancedb import LanceDBVectorStore

from dotenv import load_dotenv

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

LANCEDB_URI = f"{INPUT_DIR}/lancedb"

COMMUNITY_REPORT_TABLE = "create_final_community_reports"
ENTITY_TABLE = "create_final_nodes"
ENTITY_EMBEDDING_TABLE = "create_final_entities"
RELATIONSHIP_TABLE = "create_final_relationships"
COVARIATE_TABLE = "create_final_covariates"
TEXT_UNIT_TABLE = "create_final_text_units"
COMMUNITY_LEVEL = 2

# read nodes table to get community and degree data
entity_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_TABLE}.parquet")
entity_embedding_df = pd.read_parquet(f"{INPUT_DIR}/{ENTITY_EMBEDDING_TABLE}.parquet")

entities = read_indexer_entities(entity_df, entity_embedding_df, COMMUNITY_LEVEL)

# print("Read in the entities")

# load description embeddings to an in-memory lancedb vectorstore
# to connect to a remote db, specify url and port values.
description_embedding_store = LanceDBVectorStore(
    collection_name="entity_description_embeddings",
)
description_embedding_store.connect(db_uri=LANCEDB_URI)
entity_description_embeddings = store_entity_semantic_embeddings(
    entities=entities, vectorstore=description_embedding_store
)

# print("Embeddings")

# print(f"Entity count: {len(entity_df)}")
entity_df.head()

relationship_df = pd.read_parquet(f"{INPUT_DIR}/{RELATIONSHIP_TABLE}.parquet")
relationships = read_indexer_relationships(relationship_df)

# print(f"Relationship count: {len(relationship_df)}")
relationship_df.head()

report_df = pd.read_parquet(f"{INPUT_DIR}/{COMMUNITY_REPORT_TABLE}.parquet")
reports = read_indexer_reports(report_df, entity_df, COMMUNITY_LEVEL)

# print(f"Report records: {len(report_df)}")
report_df.head()

text_unit_df = pd.read_parquet(f"{INPUT_DIR}/{TEXT_UNIT_TABLE}.parquet")
text_units = read_indexer_text_units(text_unit_df)

# print(f"Text unit records: {len(text_unit_df)}")
text_unit_df.head()

load_dotenv()
api_key = os.getenv("api_key")
llm_model = os.getenv("llm_model")
embedding_model = os.getenv("embedding_model")

llm = ChatOpenAI(
    api_key=api_key,
    model=llm_model,
    api_type=OpenaiApiType.OpenAI,  # OpenaiApiType.OpenAI or OpenaiApiType.AzureOpenAI
    max_retries=20,
)

# print("LLM")

token_encoder = tiktoken.get_encoding("cl100k_base")

text_embedder = OpenAIEmbedding(
    api_key=api_key,
    api_base=None,
    api_type=OpenaiApiType.OpenAI,
    model=embedding_model,
    deployment_name=embedding_model,
    max_retries=20,
)

context_builder = LocalSearchMixedContext(
    community_reports=reports,
    text_units=text_units,
    entities=entities,
    relationships=relationships,
    # covariates=covariates,
    entity_text_embeddings=description_embedding_store,
    embedding_vectorstore_key=EntityVectorStoreKey.ID,  # if the vectorstore uses entity title as ids, set this to EntityVectorStoreKey.TITLE
    text_embedder=text_embedder,
    token_encoder=token_encoder,
)

# print("CXT BUILDER")

local_context_params = {
    "text_unit_prop": 0.5,
    "community_prop": 0.1,
    "conversation_history_max_turns": 5,
    "conversation_history_user_turns_only": True,
    "top_k_mapped_entities": 10,
    "top_k_relationships": 10,
    "include_entity_rank": True,
    "include_relationship_weight": True,
    "include_community_rank": False,
    "return_candidate_context": False,
    "embedding_vectorstore_key": EntityVectorStoreKey.ID,
    "max_tokens": 12_000,
}

llm_params = {
    "max_tokens": 2_000,
    "temperature": 0.0,
}

search_engine = LocalSearch(
    llm=llm,
    context_builder=context_builder,
    token_encoder=token_encoder,
    llm_params=llm_params,
    context_builder_params=local_context_params,
    response_type="multiple paragraphs",
)



def answer_query(chat, query, debug=False):
    result = search_engine.search(query)

    result_row = {
        "query": query,
        "response": result.response,
        "llm_calls": result.llm_calls,
        "prompt_tokens": result.prompt_tokens,
        #"output_tokens": result.output_tokens,
        "entities": result.context_data["entities"].head().to_json(),
        "relationships": result.context_data["relationships"].head().to_json(),
        "sources": result.context_data["sources"].head().to_json(),
        "reports": result.context_data.get("reports", pd.DataFrame()).head().to_json(),
        "claims": result.context_data.get("claims", pd.DataFrame()).head().to_json(),
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
    csv_filename = user_choice + "_local_results.csv"
    df_results.to_csv(csv_filename, index=False)
    print("Saved results to " + csv_filename)
