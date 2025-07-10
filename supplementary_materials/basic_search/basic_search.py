import pandas as pd
import asyncio
from pathlib import Path
from graphrag.config.load_config import load_config
from graphrag.api import basic_search

# Set the project directory
root_dir = Path("./mriwa_naive_rag")

# Define queries to run against the MRIWA reports
queries = [
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

async def main():
    results = []

    for query in queries:
        # Load configuration and text units
        config = load_config(root_dir)
        text_units = pd.read_parquet(root_dir / "output" / "text_units.parquet")

        print(f"Running query: {query}")
        response, context_data = await basic_search(
            config=config,
            text_units=text_units,
            query=query
        )

        # Extract context 'text' chunks from context_data["Sources"]
        context_df = context_data.get("Sources", pd.DataFrame())
        context_texts = context_df["text"].tolist() if "text" in context_df.columns else []

        # Append the result
        results.append({
            "query": query,
            "response": response,
            "context": ", ".join(context_texts)
        })

    # Convert results to DataFrame and write to CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv("basic_search_results.csv", index=False)
    print("\nSaved results to basic_search_results.csv")

# Run the async main function
asyncio.run(main())
