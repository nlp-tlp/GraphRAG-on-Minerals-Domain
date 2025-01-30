# GraphRAG on technical documents - impact of knowledge graph schema

This repository contains the code, data, and results for the paper titled "GraphRAG on technical documents - impact of knowledge graph schema" by Henri Scaffidi, Prof. Melinda Hodkiewicz, Dr. Caitlin Woods, and Nicole Roocke (2025). 

## Overview

The project assesses how 1) domain-specific knowledge graph schema, and 2) the selection of local or global GraphRAG search options, impact the quality of GraphRAG responses to questions on technical documents.

## Code

The [`code`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/code) directory of the repository contains the following:
- Python code used to run GraphRAG pipelines
- Four sub-directories, containing settings and data for each of our four GraphRAG pipelines (differing in the specified knowledge graph schema - see `entity_types` in `settings.yaml`)

## Data

The [`data`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data) directory of the repository contains the following:
- [`mriwa_report_subset_txt`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt): The .txt versions of the seven MRIWA technical reports analysed in this project. All MRIWA reports are publicly accessible at [MRIWA's Project Portfolio](https://www.mriwa.wa.gov.au/research-projects/project-portfolio/) as PDF versions. We used [PyPDF2](https://pypi.org/project/PyPDF2/) to extract the PDF text to .txt files.
- [`mriwa_cqa`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_cqa): The set of MRIWA-defined competency questions and answers used to evaluate the GraphRAG pipelines in this project.

## Results

The [`results`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/results) directory of the repository contains the GraphRAG pipelines' responses, using both local and global search, to all MRIWA-defined competency questions.

## Supplementary Materials

The [`supplementary_materials`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/supplementary_materials) directory of the repository contains the following:
- GraphRAG performance analysis marking scheme and [results](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/performance_analysis.pdf)
- [Cost analysis](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/cost_analysis.md)
- [Entity tagging example](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/entity_tagging_example.png) using a domain-specific knowledge graph schema on MRIWA report text
- [Cross-validation of our performance analysis results](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/supplementary_materials/ragas_analysis.md) using RAGAS