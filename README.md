# GraphRAG on technical documents - impact of knowledge graph schema

This repository contains the code, data, and results for the paper titled "GraphRAG on technical documents - impact of knowledge graph schema" by Henri Scaffidi, Prof. Melinda Hodkiewicz, Dr. Caitlin Woods, and Nicole Roocke (2025). 

## Overview

The project assesses how 1) domain-specific knowledge graph schema, and 2) the selection of local or global GraphRAG search options, impact the quality of GraphRAG responses to questions on technical documents.
We use [Microsoft's GraphRAG](https://github.com/microsoft/graphrag) framework for all experiments which is available under an MIT license.

## Code

The [`src`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/src) directory of the repository contains the following:
- Python code used to run GraphRAG pipelines (adapted from [Microsoft's GraphRAG Notebooks](https://microsoft.github.io/graphrag/query/notebooks/overview/))
- Four sub-directories, containing settings and data for each of our four GraphRAG pipelines (differing in the specified knowledge graph schema - see `entity_types` in `settings.yaml`)

## Data

The [`data`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/data) directory of the repository contains the following:
- [`mriwa_report_subset_txt`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/data/mriwa_report_subset_txt): The .txt versions of the 15 MRIWA technical reports analysed in this project. All MRIWA reports are publicly accessible at [MRIWA's Project Portfolio](https://www.mriwa.wa.gov.au/research-projects/project-portfolio/) as PDF versions. We used [PyPDF2](https://pypi.org/project/PyPDF2/) to extract the PDF text to .txt files.
- [`mriwa_cqa`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/data/mriwa_cqa): The set of MRIWA-defined competency questions and answers used to evaluate the GraphRAG pipelines in this project.

## Results

The [`results`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/results) directory of the repository contains the GraphRAG pipelines' responses using both local and global search, and Baseline RAG's responses, to all MRIWA-defined competency questions.

## Supplementary Materials

The [`supplementary_materials`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/supplementary_materials) directory of the repository contains the following:
- GraphRAG performance analysis marking scheme and [results](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/performance_analysis)
- [Cost analysis](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/cost_analysis.md)
- [Distribution of page count across MRIWA technical reports](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/mriwa_report_page_counts.png)
- [MRIWA report sample selection process](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/mriwa_report_sample_selection.md)
- [Baseline/Naive RAG code and settings](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/supplementary_materials/basic_search)
