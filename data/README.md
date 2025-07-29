# Data

## MRIWA Report Subset

[`mriwa_report_subset_txt`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/data/mriwa_report_subset_txt) contains the .txt versions of the 15 MRIWA technical reports analysed in this project. All MRIWA reports are publicly accessible at [MRIWA's Project Portfolio](https://www.mriwa.wa.gov.au/research-projects/project-portfolio/) as PDF versions. We used [PyPDF2](https://pypi.org/project/PyPDF2/) to extract the PDF text to .txt files.

## Competency Questions and Answers

[`mriwa_cqa`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/tree/main/data/mriwa_cqa) contains 15 .csv files, detailing our 15 MRIWA-defined competency questions and answers. Additional information to support the answers, extracted directly from MRIWA reports, are contained in the following documents:
- [`mriwa_meriwa_instances.csv`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/data/mriwa_cqa/additional_information/mriwa_meriwa_instances.csv): All mentions of "MRIWA" and "MERIWA" in each MRIWA report.
- [`nickel_instances.csv`](https://github.com/nlp-tlp/GraphRAG-on-Minerals-Domain/blob/main/data/mriwa_cqa/additional_information/nickel_instances.csv): All mentions of "Nickel" and "Ni" in each MRIWA report.
