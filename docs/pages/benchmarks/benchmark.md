---
layout: docs
header: true
seotitle: Benchmarks | LangTest | John Snow Labs
title: Available Benchmarks
key: benchmark
permalink: /docs/pages/benchmarks/benchmark
aside:
    toc: true
sidebar:
    nav: benchmarks
show_edit_on_github: true
nav_key: benchmarks
modify_date: "2019-05-16"
---


<div class="main-docs" markdown="1">
<div class="h3-box" markdown="1">

LangTest supports many benchmark datasets for testing your models. These are generally for LLM's and focus on different
abilities of LLM's such as question answering and summarization. There are also benchmarks to test a model's performance on
metrics like robustness, accuracy and fairness. 

</div><div class="h3-box" markdown="1">


{:.table2}
| Dataset                                   | Task               | Category | Source                                                                                                                                                 | Colab                                                                                                                                                                                                                                      |
| ----------------------------------------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [**ASDiv**](other_benchmarks/asdiv)                        | question-answering | `robustness`, `accuracy`, `fairness`        | [A Diverse Corpus for Evaluating and Developing English Math Word Problem Solvers](https://arxiv.org/abs/2106.15772)                                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/ASDiv_dataset.ipynb)                  |
| [**BBQ**](other_benchmarks/bbq)                            | question-answering | `robustness`, `accuracy`, `fairness`        | [BBQ Dataset: A Hand-Built Bias Benchmark for Question Answering](https://arxiv.org/abs/2110.08193)                                                    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BBQ_dataset.ipynb)                    |
| [**Bigbench**](other_benchmarks/bigbench)                  | question-answering | `robustness`, `accuracy`, `fairness`        | [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615)                                                                                                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Bigbench_dataset.ipynb)               |
| [**BoolQ**](other_benchmarks/boolq)                        | question-answering | `robustness`, `accuracy`, `fairness`,`bias`        | [BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions](https://aclanthology.org/N19-1300/)                                           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/BoolQ_dataset.ipynb)                  |
| [**CommonsenseQA**](commonsense_scenario/commonsenseqa)        | question-answering | `robustness`, `accuracy`, `fairness`        | [CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge](https://arxiv.org/abs/1811.00937)                                      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/CommonsenseQA_dataset.ipynb)          |
| [**FIQA**](legal/fiqa)                          | question-answering | `robustness`, `accuracy`, `fairness`        | [FIQA (Financial Opinion Mining and Question Answering)](https://huggingface.co/datasets/explodinggradients/fiqa)                                                    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Fiqa_dataset.ipynb)                |
| [**HellaSwag**](commonsense_scenario/hellaswag)                | question-answering | `robustness`, `accuracy`, `fairness`        | [HellaSwag: Can a Machine Really Finish Your Sentence?](https://aclanthology.org/P19-1472/)                                                            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/HellaSwag_Question_Answering.ipynb)   |
| [**Consumer-Contracts**](legal/consumer-contracts)              | question-answering | `robustness`, `accuracy`, `fairness`        | [Answer yes/no questions on the rights and obligations created by clauses in terms of services agreements.](https://github.com/HazyResearch/legalbench/tree/main/tasks/consumer_contracts_qa)                                                                                                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LegalQA_Datasets.ipynb)               |
| [**Contracts**](legal/contracts)              | question-answering | `robustness`, `accuracy`, `fairness`        | [Answer yes/no questions about whether contractual clauses discuss particular issues.](https://github.com/HazyResearch/legalbench/tree/main/tasks/contract_qa)                                                                                                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LegalQA_Datasets.ipynb)               |
| [**Privacy-Policy**](legal/privacy-policy)              | question-answering | `robustness`, `accuracy`, `fairness`        | [Given a question and a clause from a privacy policy, determine if the clause contains enough information to answer the question.](https://github.com/HazyResearch/legalbench/tree/main/tasks/privacy_policy_qa)                                                                                                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LegalQA_Datasets.ipynb)               |
| [**LogiQA**](other_benchmarks/logiqa)                      | question-answering | `robustness`, `accuracy`, `fairness`        | [LogiQA: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning](https://paperswithcode.com/paper/logiqa-a-challenge-dataset-for-machine)                                                                                            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/LogiQA_dataset.ipynb)                 |
| [**MMLU**](other_benchmarks/mmlu)                          | question-answering | `robustness`, `accuracy`, `fairness`        | [MMLU: Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)                                                           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/mmlu_dataset.ipynb)                   |
| [**NarrativeQA**](other_benchmarks/narrativeqa)            | question-answering | `robustness`, `accuracy`, `fairness`        | [The NarrativeQA Reading Comprehension Challenge](https://aclanthology.org/Q18-1023/)                                                                  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/NarrativeQA_Question_Answering.ipynb) |
| [**NQ-open**](other_benchmarks/nq-open) | question-answering | `robustness`, `accuracy`, `fairness`        | [Natural Questions: A Benchmark for Question Answering Research](https://aclanthology.org/Q19-1026/)                                                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/NQ_open_dataset.ipynb)                |
| [**OpenBookQA**](commonsense_scenario/openbookqa)              | question-answering | `robustness`, `accuracy`, `fairness`        | [Can a Suit of Armor Conduct Electricity? A New Dataset for Open Book Question Answering](https://arxiv.org/abs/1809.02789)                                                                                            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/OpenbookQA_dataset.ipynb)             |
| [**PIQA**](commonsense_scenario/piqa)                          | question-answering | `robustness`        | [PIQA: Reasoning about Physical Commonsense in Natural Language](https://arxiv.org/abs/1911.11641)                                                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/PIQA_dataset.ipynb)                   |
| [**Quac**](other_benchmarks/quac)                          | question-answering | `robustness`, `accuracy`, `fairness`        | [Quac: Question Answering in Context](https://aclanthology.org/D18-1241/)                                                                              | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/quac_dataset.ipynb)                   |
| [**SIQA**](commonsense_scenario/siqa)                          | question-answering | `robustness`, `accuracy`, `fairness`        | [SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728)                                                         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/SIQA_dataset.ipynb)                   |
| [**TruthfulQA**](other_benchmarks/truthfulqa)              | question-answering | `robustness`, `accuracy`, `fairness`        | [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://aclanthology.org/2022.acl-long.229/)                                                 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/TruthfulQA_dataset.ipynb)             |
| [**XSum**](other_benchmarks/xsum)                          | summarization      | `robustness`, `accuracy`, `fairness`, `bias`        | [Don’t Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](https://aclanthology.org/D18-1206/) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/XSum_dataset.ipynb)                   |
| [**MultiLexSum**](legal/multilexsum)            | summarization      | `robustness`, `accuracy`, `fairness`        | [Multi-LexSum: Real-World Summaries of Civil Rights Lawsuits at Multiple Granularities](https://arxiv.org/abs/2206.10883)                              | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/MultiLexSum_dataset.ipynb)            |
| [**MedMCQA**](medical/medmcqa)              | question-answering | `robustness`, `accuracy`, `fairness`        | [MedMCQA: A Large-scale Multi-Subject Multi-Choice Dataset for Medical domain Question Answering](https://proceedings.mlr.press/v174/pal22a)  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             |
| [**MedQA**](medical/medqa)              | question-answering | `robustness`, `accuracy`, `fairness`        | [What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams](https://paperswithcode.com/dataset/medqa-usmle) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             |
| [**PubMedQA**](medical/pubmedqa)              | question-answering | `robustness`, `accuracy`, `fairness`        | [PubMedQA: A Dataset for Biomedical Research Question Answering](https://arxiv.org/abs/1909.06146)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             | 
| [**LiveQA**](medical/liveqa)              | question-answering | `robustness`        | [Overview of the Medical Question Answering Task at TREC 2017 LiveQA](https://trec.nist.gov/pubs/trec26/papers/Overview-QA.pdf)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             | 
| [**MedicationQA**](medical/medicationqa)              | question-answering | `robustness`        | [Bridging the Gap Between Consumers' Medication Questions and Trusted Answers](https://pubmed.ncbi.nlm.nih.gov/31437878/)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             | 
| [**HealthSearchQA**](medical/healthsearchqa)              | question-answering | `robustness`        | [Large Language Models Encode Clinical Knowledge](https://paperswithcode.com/paper/large-language-models-encode-clinical)| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnSnowLabs/langtest/blob/main/demo/tutorials/llm_notebooks/dataset-notebooks/Medical_Datasets.ipynb)             | 

</div>