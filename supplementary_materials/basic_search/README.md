### Requirements

Python 3.10-3.12

### Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate a virtual environment:
  - **macOS/Linux:**  
    ```bash
    source venv/bin/activate
    ```
  - **Windows (Command Prompt):**  
    ```cmd
    venv\Scripts\activate
    ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. In the `mriwa_naive_rag` directory, copy the contents of `.env.example` to a new file in the same folder named `.env`. Add your OpenAI API key (to use `gpt-4o-mini`) to the `.env` file by setting `api_key = <your_key>`.

### Indexing

> Note: This process may take hours and can be expensive depending on the size of the input and LLM used. It is not recommended to run this process if you only want to use the GraphRAG package for Naive RAG, as the indexing process builds a knowledge graph which isn't used during Naive RAG.

1. Run indexing pipeline:
   ```bash
   graphrag index --method fast --root ./mriwa_naive_rag
   ```

### Query

Running the following script will ask all 15 MRIWA competency questions using Baseline "Naive" RAG and results are saved to a .csv file.

- To run **basic search**:
  ```bash
  python basic_search.py
  ```

### Additional Notes

- The `mriwa_naive_rag` directory and its contents are generated using [Microsoft's GraphRAG](https://github.com/microsoft/graphrag) framework. The content we alter/provide include:
   - MRIWA reports in `/input` for all pipelines.
   - `model` in `settings.yaml` for all pipelines to `gpt-4o-mini`.

