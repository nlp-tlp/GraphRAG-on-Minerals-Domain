# Competency Questions and Answers

## Keyword Search Queries
- **Identify which MRIWA reports reference MERIWA or MRIWA.**
  - **Answer:** All have MRIWA in the document. None have MERIWA referenced.
- **Extract all references to MERIWA and MRIWA from the MRIWA reports.**
  - **Answer:** See [`Extracted MRIWA References`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/blob/main/data/mriwa_cqa/mriwa_references.md).
- **Identify any references to nickel or Ni in the MRIWA reports.**
  - **Answer:** See X. MRIWA reports with substantial amounts of Nickel mentions: [`432`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_432_MRIWA_M0432.txt), [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt), [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt), [`451`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_451_MRIWA_M0451.txt).
- **Which MRIWA report is related to the East Kimberley region?**
  - **Answer:** [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt) (very minimal mention, hardly related) and [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt) (in the title, important).

## Aggregation Queries

- **Which elements are considered in the MRIWA reports?**
  - **Answer:** A useful response may identify all reports and state, for each report, the elements that are mentioned lots. See X. 
    - **Most mentioned elements:** Iron, Sulfur, Gold, Copper, Oxygen, Nickel, Gold, Silver, Lithium, Tantalum.
- **Which MRIWA report author has been involved in more than one report/project?**
  - **Answer:** 
    - BARRY PRICE  
    - DAVID ALLEN  
    - NOREEN EVANS  
    - RAJESH SHARMA  
    - SILVIA BLACK  
    - BRENT MCINNES
  - See X for all authors.
- **What is the average number of references in each MRIWA report?**
  - **Answer:** 197.

## Complex Semantic Queries

- **Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with in any capacity (including being listed in references)?**
  - **Answer:** 
    - [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt)
    - [`451`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_451_MRIWA_M0451.txt)
    - [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt)
    - [`488`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_488_MRIWA_M0488.txt)
    - [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt)
    - [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt)
- **Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a researcher?**
  - **Answer:**
    - [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt)
    - [`488`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_488_MRIWA_M0488.txt)
    - [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt)
- **Which MRIWA reports has Commonwealth Scientific Industrial Research Organisation been involved with as a sponsor?**
  - **Answer:** None.
- **Which regions of Western Australia are referenced in the MRIWA reports?**
  - **Answer:** 
    - State Government Regions:
      - Kimberley: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt) and [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt)
      - Goldfields: [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt), [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt), [`432`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_432_MRIWA_M0432.txt)
      - Pilbara: [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt), [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt), [`432`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_432_MRIWA_M0432.txt)
      - North West ([`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt), [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt))
      - Mid West
      - South West ([`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`451`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_451_MRIWA_M0451.txt)) – as a direction not location ([`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt))
    - Geological/Tectonic regions are also mentioned, commonly including:
      - Pilbara: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt)
      - Yilgarn: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt)
      - Kimberley: [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt)
      - Canning: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`488`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_488_MRIWA_M0488.txt)
      - Officer: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt)
      - Musgrave: [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt)
      - Halls Creek: [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt)
- **Which MRIWA reports relate to leaching?**
  - **Answer:** [`432`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_432_MRIWA_M0432.txt), [`451`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_451_MRIWA_M0451.txt), [`488`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_488_MRIWA_M0488.txt), [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt) (minor mentions)
- **Which MRIWA reports relate to exploration?**
  - **Answer:** [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt), [`459-489`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_459-489_MRIWA_M0459-M0484.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt)
- **Which MRIWA reports relate to mining extraction?**
  - **Answer:** 
    - [`488`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_488_MRIWA_M0488.txt), [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt), [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt) (mentions of Li extraction), [`432`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_432_MRIWA_M0432.txt) (mentions of extraction procedure)
- **Which MRIWA reports relate to mineral processing?**
  - **Answer:** [`532`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_532_MRIWA_M0532.txt), [`448`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_448_MRIWA_M0448.txt) (ISR), [`505`](https://github.com/nlp-tlp/KGschema_eval_4GraphRAG/tree/main/data/mriwa_report_subset_txt/Final-Report_505_MRIWA_M0505.txt)
