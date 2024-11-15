import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json


# HEADLESS MODE options --------------------------------------------
def web_driver(webdriver, headless):
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    if headless:
        options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver


# JSON -------------------------------------------------------------------
def load_and_read_json(fpath) -> list:
    with open (fpath, "r") as f:
        q = json.load(f)
    qList = []
    for i in range(len(q)):
        qList.append(q[i]['question'])
    return qList


# --------------- QUERY -> URLs ---------------- #
# INPUT: STRING
def search_and_collect_urls(query: str, top_n=1): 
    """
    1. initialize driver and go to google.com
    2. search box -> enter the query -> submit
    3. find all the text using CSS Selector
    4. collect the url from the page
    5. list -> set -> list ---> return urls
    """
    driver = web_driver(webdriver)
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g a')
    driver.quit()
    
    urls = []
    for result in search_results:
        url = result.get_attribute('href')
        if url and url.startswith('http') and 'google.com' not in url:
            urls.append(url)
    top_n_urls = urls[:top_n]
    urls = list(set(top_n_urls))
    return urls


#INPUT: LIST
def search_and_collect_all_urls(query_list: list, top_n=4, headless=True): 

    driver = web_driver(webdriver, headless)
    all_urls = []
    i=1
    for q in query_list:
        driver.get("https://www.google.com")
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(q)
        search_box.send_keys(Keys.ENTER)
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g a')
        time.sleep(1)
        urls = []
        for r in search_results:
            url = r.get_attribute('href')
            if url and 'google.com' not in url:
                urls.append(url)
            if len(urls) >= top_n:
                break

        for url in urls:
            all_urls.append(url)
        i+=1

    driver.quit()
    
    return all_urls[:top_n*i]

