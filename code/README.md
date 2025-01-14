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

> Note: This process may take hours and can be expensive depending on the size of the input and LLM used. 

1. In each of the four schema directories, `.env` contains GRAPHRAG_API_KEY=<API_KEY> which should be replaced by your own OpenAI API key

2. Run indexing pipeline using Generalised Schema:
   ```bash
   python -m graphrag.index --root ./generalised_schema
   ```
   Run indexing pipeline using Expanded Schema:
   ```bash
   python -m graphrag.index --root ./expanded_schema
   ```
   Run indexing pipeline using Auto-Generated Schema:
   ```bash
   python -m graphrag.index --root ./auto_generated_schema
   ```
   Run indexing pipeline using Schema-less pipeline:
   ```bash
   python -m graphrag.index --root ./schema_less
   ```

### GraphRAG Query

Running the following scripts will allow you to select which schema's index to query. By default, all 15 MRIWA competency questions are asked and results are printed to stdout.

- To run **local search**:
  ```bash
  python local_search.py
  ```

- To run **global search**:
  ```bash
  python global_search.py
  ```