`results.csv` contains the following fields:
- `question`: The MRIWA-defined competency question asked to the GraphRAG pipeline.
- `response`: The response provided by the GraphRAG pipeline to the `question`.
- `schema`: The knowledge graph schema used in the GraphRAG pipeline, being one of the following:
    1. **Minerals Domain Schema (MDS)**: 
        `{naturally_occurring_object,processed_object,process,organisation,site_location_boundary}`
    2. **Expanded Minerals Domain Schema (EMDS)**: 
        `{natural_process,lab_process,industrial_process,naturally_occurring_object,processed_material,manufactured_product,site_location_boundary,organisation}`
    3. **Auto-Generated Schema (AS)**: 
        `{chemical process,mineral,geological survey,geochemistry,exploration technique,sample,formation,project,research study}`
    4. **Schema-less (SL)**
- `search_technique`: The GraphRAG search technique used in the GraphRAG pipeline, being either local or global search.
