# Validation of Performance Analysis using Retrieval Augmented Generation Assessment (RAGAS)

Further, we utilise [`Retrieval Augmented Generation Assessment (RAGAS)`](https://github.com/explodinggradients/ragas) to evaluate the reliability of results. This framework utilises LLMs to produce evaluation metrics about RAG pipelines. We measure `answer_correctness` in all responses to the same question, "Which MRIWA report is related to the East Kimberley region?", compared to an ideal answer. The score ranges from 0 to 1, and a higher score indicates closer alignment between the pipeline response and the ideal answer. This analysis is conducted three times and the average results are displayed in Table 1.

## Table 1: Results of RAGAS evaluation on pipeline answers to the question, "Which MRIWA report is related to the East Kimberley region?"

|                   | MDS | EMDS | AS | SL |
|-------------------|--------|--------|--------|--------|
| answer_correctness | **0.66** | 0.61   | 0.48   | 0.61   |

The results indicate that the MDS pipeline produces responses that are more correct than other pipeline responses. This finding is consistent with our performance analysis.



