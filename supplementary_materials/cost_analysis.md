# Cost Analysis

Our MDS pipeline, using GPT-4o-Mini, cost 15.57 AUD to run the *Indexing* phase once and to run 15 local search queries and 15 global search queries (a breakdown of these costs is displayed in Table 1 and Table 2). Our global search queries cost approximately 0.17 AUD each, whilst local search queries cost approximately 0.01 AUD each. The total cost to run the four-pipeline experiment was 60.22 AUD.

## Table 1: Indexing statistics for Minerals Domain Schema pipeline.

| Words Ingested | Tokens (context and generated) | OpenAI API Requests | Cost (AUD) |
|---------------|--------------------------------|----------------------|------------|
| 1,064,496    | 54,528,382                      | 30,198               | 13.07      |

## Table 2: Query statistics for Minerals Domain Schema pipeline.

| Tokens (context and generated) | OpenAI API Requests | Cost (AUD) |
|--------------------------------|----------------------|------------|
| 16,400,000                     | 1319                 | 2.50       |

