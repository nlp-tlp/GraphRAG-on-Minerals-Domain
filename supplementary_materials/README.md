# Supplementary Materials

This directory contains the following supplementary materials for the paper titled "GraphRAG on technical documents - impact of knowledge graph schema" by Henri Scaffidi, Prof. Melinda Hodkiewicz, Dr. Caitlin Woods, and Nicole Roocke (2025). 

- [`Cost Analysis`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/cost_analysis.md): An analysis of both monetary and computation costs of our experiments.
- [`Entity Tagging Example`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/entity_tagging_example.png): An example of our Minerals Domain Schema being  (manually) used to tag entities in MRIWA report text.
- [`Performance Analysis`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/performance_analysis.pdf): The full results of our GraphRAG performance analysis using the marking scheme below.

| Code | Name                     | Criteria |
|------|--------------------------|-----------------------------------------------------------|
| B1   | High Answer Relevance    | All ideal answer information is present in the response. |
| B2   | Medium Answer Relevance  | Some ideal answer information is present in the response. |
| B3   | Medium Noise Robustness  | Some factually correct information that is closely related to the question, but that does not directly answer the question, is present in the response. |
| B4   | Low Noise Robustness     | Some factually correct information that is irrelevant to the question is present in the response. |
| B5   | Hallucination            | A hallucination is present in the response. |

- [`RAGAS Analysis`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/ragas_analysis.md): An analysis of our GraphRAG results using RAGAS to cross-validate.