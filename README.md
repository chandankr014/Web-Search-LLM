
# Web Search Module - LOGSTRIKE TECHNOLOGIES

This repository contains a web search module for extracting and parsing web content. Follow the steps below to run the module and process data.

## Steps to Run the Module:

### Step 1: Run the Scraper

The scraping process is handled by the **ScrapGraph** tool. **ScrapGraph** uses **Selenium** to automate web browsers and extract data from web-pages with the power of build-in LLM for extarcting contexts from web-pages. 

To start the scraping process, run the following command:

```bash
python ScrapGraph.py
```

This script will initiate the scraper and gather information from the specified URLs. The scraper can run in **headless mode**, meaning it operates without opening a visible browser window, making it more efficient for automation on servers or systems without GUI support.

**Selenium** is used in this module to:
- Automate browser interactions such as navigating through pages, clicking elements, and extracting content.
- Perform scraping in headless mode for faster performance and seamless execution in the background.

If you'd like to enable headless mode, ensure that the browser options in the **ScrapGraph.py** script are set accordingly:

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enables headless mode
driver = webdriver.Chrome(options=options)
```

### Step 2: Run the Parser

Once the scraping process is complete, the next step is to parse the gathered data. To do so, navigate to the `Parser` directory and run the parser script:

```bash
cd Parser
python parser.py
```

The parser processes the whole web-content, images, scripts, and urls

## Output Files

During runtime, the following files are automatically generated and stored in the project directory:

### ScrapGraph.py
- **answers**: List of contents extarcted from selected webpages.
- **artifacts**: uses created answers to build a Final Answer. levarages LLM for this task.
- **URLs**: A collection of the web links that were visited and scraped. stored in JSON format.

### parser.py
- **res**: contains the parsed domain names and its all parsed data

## Technologies Used

### Selenium

Selenium is a powerful tool for automating web browsers. It allows developers to simulate user interactions with a website, such as clicking buttons, filling forms, or scraping data from specific elements on a page. Selenium is especially useful for scraping dynamic content that requires interaction with JavaScript.

- **Headless Mode**: This feature allows Selenium to run without a GUI. It's ideal for use cases where a browser window is not needed, such as server-based applications, continuous integration environments, or remote scraping tasks.

## Collaboration and Credit

If you'd like to collaborate or need more information, feel free to contact us at:

**chandankr014@gmail.com**
