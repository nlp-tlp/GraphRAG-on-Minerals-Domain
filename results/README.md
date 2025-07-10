# Results

The `experiment_two` folder contains the latest results.

Within `experiment_two`, each directory contains the results for one GraphRAG pipeline using a specific knowledge graph schema. The schemas are as follows.
1. **Minerals Domain Schema (MDS)**: 
    `{naturally_occurring_object,processed_object,process,organisation,site_location_boundary}`
2. **Expanded Minerals Domain Schema (EMDS)**: 
    `{natural_process,lab_process,industrial_process,naturally_occurring_object,processed_material,manufactured_product,site_location_boundary,organisation}`
3. **Auto-Generated Schema (AS)**: 
    `{chemical process,mineral,geological survey,geochemistry,exploration technique,sample,formation,project,research study}`
4. **Schema-less (SL)**

Each schema directory contains two `.csv` files (one for **local search** pipelines, and another for **global search** pipelines) with two fields:
- `query`: The MRIWA-defined competency question asked to the GraphRAG pipeline.
- `response`: The response provided by the GraphRAG pipeline to the query.

The `.csv` files also contain additional statistics and the context that was used to answer the query.

The directory `Naive_RAG_results` contains results for the pipeline using **basic search**, a vector similarity search implementation.


