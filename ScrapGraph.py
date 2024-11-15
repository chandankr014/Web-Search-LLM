import ast
import json
from scrapegraphai.graphs import SmartScraperGraph
from scripts.selenium import search_and_collect_all_urls, search_and_collect_urls
from scripts.common import get_common_domain_urls, save_json, save_markdown, save_urls
from scripts.model import MODEL, invoke_query
from optimization.query import rephrase_n_query, invoke_intent
from optimization.switch import Switcher
import ast
import json


class IntentHandler:
    def __init__(self, query):
        self.query = query
        self.intent = self.invoke_intent()
        self.switcher = Switcher()
        self.prompt = self.switcher.Switch(intent=self.intent, query=self.query)

    def invoke_intent(self):
        return invoke_intent(query=self.query, log=True)


class UrlFetcher:
    def __init__(self, query, intent, N, TOP_N, HEADLESS_MODE):
        self.query = query
        self.intent = intent
        self.N = N
        self.TOP_N = TOP_N
        self.HEADLESS_MODE = HEADLESS_MODE
        self.urls = []

    def fetch_urls(self):
        llm_output = rephrase_n_query(query=self.query, N=self.N)
        queries_list = ast.literal_eval(llm_output)

        if len(queries_list) == self.N:
            all_urls = search_and_collect_all_urls(query_list=queries_list, top_n=self.TOP_N, headless=self.HEADLESS_MODE)
            self.urls = all_urls
            # save_urls(urls=self.urls, all_urls=None if not self.urls else self.urls)
        else:
            print("Error: Number of URLs fetched is inconsistent. Trying with the Query Web-Search in HEAD Mode")
            self.urls = self.search_and_collect_urls(self.query)
            # save_urls(urls=self.urls, all_urls=None if not self.urls else self.urls)


class Scraper:
    def __init__(self, urls, prompt, api_key, model, headless_mode):
        self.urls = urls
        self.prompt = prompt
        self.graph_config = {
            "llm": {
                "api_key": api_key,
                "model": model,
            },
            "verbose": True,
            "headless": headless_mode,
        }
        self.response = {"answer": []}

    def run_scraping(self):
        for url in self.urls:
            smart_scraper_graph = SmartScraperGraph(
                prompt=self.prompt,
                source=url,
                config=self.graph_config
            )
            result = smart_scraper_graph.run()
            self.response["answer"].append(result)

    def combine_answers(self):
        return " ".join(json.dumps(item) for item in self.response["answer"])


class ResponseHandler:
    def __init__(self, combined_answer, query):
        self.combined_answer = combined_answer
        self.query = query

    def invoke_llm(self):
        return invoke_query(
            question=self.query,
            context=self.combined_answer
        )

    def save_answer(self, answer):
        try:
            save_markdown(data=str(answer))
        except Exception as e:
            save_json(data=answer)

    def to_markdown(self, ai_message):
        try:
            print("Formatting AIMessage")
            message_dict = {
                "role": ai_message.role,
                "content": ai_message.content,
                "additional_fields": {
                    key: value for key, value in vars(ai_message).items()
                    if key not in ['role', 'content']
                }
            }
            # Generate a Markdown string
            # markdown_output = f"**Role**: {message_dict['role']}\n\n"
            markdown_output = f"\n{message_dict['content']}\n"
            print(markdown_output)
            return markdown_output
        except Exception:
            return "Input is not an AIMessage object."

# to be called
def main(query, N, TOP_N, API_KEY, MODEL, HEADLESS_MODE):
    print("##-------------------------- AGENT Started --------------------------")
    intent_handler = IntentHandler(query)
    url_fetcher = UrlFetcher(query, intent_handler.intent, N, TOP_N, HEADLESS_MODE)
    url_fetcher.fetch_urls()
    # url_fetcher.get_common_domain_urls()

    scraper = Scraper(url_fetcher.urls, intent_handler.prompt, API_KEY, MODEL, HEADLESS_MODE)
    scraper.run_scraping()
    
    combined_answer = scraper.combine_answers()
    response_handler = ResponseHandler(combined_answer, query)
    answer = response_handler.invoke_llm()
    print("##-------------------------- AGENT Stopped --------------------------")
    return answer.content

# calling
# main(query="IIT vs IIM", N=5, TOP_N=10, API_KEY=API_KEY, MODEL=MODEL)
