# Data

## MRIWA Report Subset

[`mriwa_report_subset_txt`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt) contains the .txt versions of the seven MRIWA technical reports analysed in this project. All MRIWA reports are publicly accessible at [MRIWA's Project Portfolio](https://www.mriwa.wa.gov.au/research-projects/project-portfolio/) as PDF versions. We used [PyPDF2](https://pypi.org/project/PyPDF2/) to extract the PDF text to .txt files.

## Competency Questions and Answers

[`mriwa_cqa`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_cqa) contains [`questions_answers.md`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/questions_answers.md), detailing our 15 MRIWA-defined competency questions and answers. Additional information to support the answers, extracted directly from MRIWA reports, are contained in the following documents:
- [`authors.md`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/authors.md): All authors of each MRIWA report (in our subset).
- [`chemical_elements.md`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/chemical_elements.md): Counts of chemical elements mentioned (by name) in each MRIWA report.
- [`mriwa_references.md`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/mriwa_references.md): All mentions of "MRIWA" and "Minerals Research Institute of Western Australia" in each MRIWA report.
- [`nickel_references.md`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/nickel_references.md): All mentions of "Nickel" and "Ni" in each MRIWA report.
