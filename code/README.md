### Requirements

Python 3.10-3.12

### Environment Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to the `.env` file by setting `OPENAI_API_KEY=<your_key>`

### GraphRAG Indexing

> These steps are based on the following tutorial: [GraphRAG - Getting Started](https://microsoft.github.io/graphrag/get_started/). Note: This process may take hours and can be expensive depending on the size of the input and LLM used. 

1. Make directory:
   ```bash
   mkdir -p ./ragtest/input
   ```

2. Place .txt files from `./mriwa_report_subset` in `./ragtest/input`

3. Setup workspace variables:
   ```bash
   graphrag init --root ./ragtest
   ```

   - Within `./ragtest` directory, .env contains GRAPHRAG_API_KEY=<API_KEY> which should be replaced by your own OpenAI API key
   - Replace `settings.yaml` file in `./ragtest` directory with the `settings.yaml` from `./schema_settings` of your desired schema
   - If running the Schema-less pipeline, also replace `entity_extraction.txt` in `./ragtest/prompts` with `entity_extraction.txt` from `./schema_settings/schemaless`

4. Run indexing pipeline:
   ```bash
   graphrag index --root ./ragtest
   ```

### GraphRAG Query

- To run **local search**:
  ```bash
  python local_search.py
  ```

- To run **global search**:
  ```bash
  python global_search.py
  ```