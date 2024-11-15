"""
SmartScraperGraph:      Single-page scraper that only needs a user prompt and an input source.
SearchGraph:            Multi-page scraper that extracts information from the top n search results of a search engine.
SpeechGraph:            Single-page scraper that extracts information from a website and generates an audio file.
ScriptCreatorGraph:     Single-page scraper that extracts information from a website and generates a Python script.
SmartScraperMultiGraph: Multi-page scraper that extracts information from multiple pages given a single prompt and a list of sources.
ScriptCreatorMultiGraph:Multi-page scraper that generates a Python script for extracting information from multiple pages and sources.


if len(queries_list) == N:
    all_urls = []
    for qr in queries_list:
        urls = search_and_collect_urls(query=qr, top_n=TOP_N)
        all_urls.append(urls)
    urls = get_common_items(all_urls)
    save_urls(urls=urls, all_urls=all_urls)
"""

from evaluation.prompt import *
from scripts.model import invoke_prompt
query = "Do research on how to find the response relevance of LLM"
response = "## Evaluating Response Relevance of LLMs: A Deep Dive\n\nThis question delves into the crucial aspect of evaluating the quality of Large Language Model (LLM) responses. While LLMs are impressive in their ability to generate human-like text, assessing the relevance of their outputs is a complex task. Here's a detailed breakdown of the core concepts and their interdependencies:\n\n**1. Understanding Response Relevance:**\n\n* **Definition:** Response relevance refers to how well an LLM's generated text aligns with the user's intent and the context of the query. It's about the output being informative, accurate, and directly addressing the user's need.\n* **Importance:**  Accurate assessment of relevance is vital for:\n    * **Trustworthiness:** Users need to be confident that the LLM provides reliable information.\n    * **User Experience:** Irrelevant responses frustrate users and diminish the value of the LLM.\n    * **Model Improvement:** Evaluating relevance helps identify areas where the LLM needs improvement.\n\n**2. Challenges in Evaluating Relevance:**\n\n* **Subjectivity:**  Relevance is often subjective. What's relevant to one user might not be to another.\n* **Contextual Dependence:**  Relevance is highly dependent on the specific query, context, and user expectations.\n* **Open-Endedness:**  LLMs can generate creative and unexpected responses. Evaluating their relevance can be challenging when the output is not directly aligned with a specific answer.\n\n**3. Methods for Evaluating Response Relevance:**\n\n* **Human Evaluation:** \n    * **Direct Assessment:** Human judges evaluate the relevance of LLM responses based on predefined criteria. This is considered the gold standard but can be time-consuming and expensive.\n    * **Crowdsourcing:**  Leveraging large groups of people to evaluate responses, providing a more cost-effective approach.\n* **Automatic Evaluation Metrics:**\n    * **Extrinsic Metrics:**  Focus on the task performance of the LLM. For example, in question answering, metrics like accuracy and F1-score measure how well the LLM answers the question correctly.\n    * **Intrinsic Metrics:**  Focus on the quality of the generated text itself. These metrics include:\n        * **BLEU (Bilingual Evaluation Understudy):** Measures the overlap between the generated text and a set of reference texts.\n        * **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**  Focuses on the recall of n-grams (sequences of words) from reference texts.\n        * **METEOR (Metric for Evaluation of Translation with Explicit Ordering):**  Considers both word order and semantic similarity.\n        * **BERTscore:**  Utilizes a pre-trained language model (BERT) to assess semantic similarity between the generated text and reference texts.\n\n**4. Relationships and Dependencies:**\n\n* **Human Evaluation and Automatic Metrics:**  Human evaluation is often used to ground automatic metrics. Metrics are calibrated and improved based on human judgments.\n* **Context and Relevance:**  The context of the query heavily influences the relevance of the response. Contextual information is crucial for both human and automatic evaluation.\n* **Task and Evaluation Metrics:**  The choice of evaluation metric depends on the specific task the LLM is performing. For example, BLEU might be suitable for machine translation, while F1-score is more appropriate for question answering.\n\n**5. Future Directions:**\n\n* **Developing more robust and context-aware automatic metrics:**  This would reduce the reliance on human evaluation and enable faster and more efficient assessment of LLM performance.\n* **Integrating user feedback into evaluation:**  Capturing user preferences and understanding their expectations can improve the relevance of LLM responses.\n* **Developing new evaluation methodologies:**  Exploring novel approaches to assess the relevance of creative and open-ended LLM outputs.\n\n**Conclusion:**\n\nEvaluating the relevance of LLM responses is a crucial aspect of ensuring their trustworthiness and usability. While human evaluation remains the gold standard, automatic metrics are becoming increasingly sophisticated.  Understanding the complexities of relevance, the limitations of current methods, and the ongoing research in this area is essential for advancing the field of LLM development and application. "
prompt = evaluation_prompt(query, response)
scores = invoke_prompt(PROMPT=prompt)
print(scores)

