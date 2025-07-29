# Supplementary Materials

This directory contains the following supplementary materials for the paper titled "GraphRAG on technical documents - impact of knowledge graph schema" by Henri Scaffidi, Prof. Melinda Hodkiewicz, Dr. Caitlin Woods, and Nicole Roocke (2025). 

- [`Basic Search`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/basic_search): The code and settings used to conduct our Baseline RAG comparison.
- [`Cost Analysis`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/cost_analysis.md): An analysis of both monetary and computation costs of our experiments.
- [`MRIWA Report Page Counts`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/mriwa_report_page_counts.png): Distribution of page count across MRIWA technical reports.
- [`MRIWA Report Sample Selection`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/mriwa_report_sample_selection.md): Entity analysis of our selected MRIWA Report sample for this project.
- [`Performance Analysis`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/performance_analysis): The full results of our GraphRAG performance analysis using the following marking scheme:

| Code | Name                     | Criteria |
|------|--------------------------|-----------------------------------------------------------|
| B1   | High Answer Relevance    | All ideal answer information is present in the response. |
| B2   | Medium Answer Relevance  | Some ideal answer information is present in the response. |
| B3   | Medium Noise Robustness  | Some factually correct information that is closely related to the question, but that does not directly answer the question, is present in the response. |
| B4   | Low Noise Robustness     | Some factually correct information that is irrelevant to the question is present in the response. |
| B5   | Hallucination            | A hallucination is present in the response. |

Each pipeline (using a specific schema and search technique) was asked the following questions:

1. Identify which MRIWA reports reference MERIWA or MRIWA.
2. Extract all references to MERIWA and MRIWA from the MRIWA reports.
3. Identify any references to nickel or Ni in the MRIWA reports.
4. Which elements are considered in the MRIWA reports?
5. Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with in any capacity (including being listed in references)?
6. Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a researcher?
7. Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a sponsor?
8. Which MRIWA report is related to the East Kimberley region?
9. Which regions of Western Australia are referenced in the MRIWA reports?
10. Which MRIWA report author has been involved in more than one report/project?
11. What is the average number of references in each MRIWA report?
12. Which MRIWA reports relate to leaching?
13. Which MRIWA reports relate to exploration?
14. Which MRIWA reports relate to mining extraction?
15. Which MRIWA reports relate to mineral processing?