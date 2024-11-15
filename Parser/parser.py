import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.parse
import re
import json


# HEADLESS MODE options --------------------------------------------
def web_driver(webdriver):
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

def extract_urls_from_script(script_content):
    # Regular expression to find all HTTP/HTTPS URLs
    url_pattern = re.compile(r'https?://[^\s\'"<>]+')
    urls = url_pattern.findall(script_content)
    return urls

def fetch_and_save_webpage_content(url):
    driver = web_driver(webdriver)
    driver.get(url)
    
    # Allow time for dynamic content to load
    time.sleep(5)
    
    # Get the page source
    html_content = driver.page_source
    
    # Parse domain name
    domain = urllib.parse.urlparse(url).netloc
    
    # Create directories if they don't exist
    domain_dir = os.path.join('res', domain)
    os.makedirs(domain_dir, exist_ok=True)
    os.makedirs(os.path.join(domain_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(domain_dir, 'scripts'), exist_ok=True)  # Create scripts directory
    
    # Save HTML content as text
    txt_filename = os.path.join(domain_dir, 'page_source.txt')
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Parse HTML and find images
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    
    # Download and save images
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            if not img_url.startswith(('http://', 'https://')):
                img_url = urllib.parse.urljoin(url, img_url)
            
            try:
                img_data = requests.get(img_url, timeout=10).content
                img_filename = os.path.join(domain_dir, 'images', os.path.basename(urllib.parse.urlparse(img_url).path))
                with open(img_filename, 'wb') as f:
                    f.write(img_data)
            except Exception as e:
                print(f"Error downloading image {img_url}: {e}")
    
    # Dictionary to store URLs based on time of occurrence
    urls_dict = {}
    
    # Find and download JS/TS files
    script_tags = soup.find_all('script', src=True)
    for script in script_tags:
        script_url = script['src']
        if not script_url.startswith(('http://', 'https://')):
            script_url = urllib.parse.urljoin(url, script_url)
        
        try:
            script_data = requests.get(script_url, timeout=10).content
            script_filename = os.path.join(domain_dir, 'scripts', os.path.basename(urllib.parse.urlparse(script_url).path))
            with open(script_filename, 'wb') as f:
                f.write(script_data)
            
            # Extract URLs from the script content
            script_content = script_data.decode('utf-8', errors='ignore')
            urls = extract_urls_from_script(script_content)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            urls_dict[timestamp] = urls
        except Exception as e:
            print(f"Error downloading script {script_url}: {e}")
    
    # Save URLs to a JSON file
    json_filename = os.path.join(domain_dir, 'extracted_urls.json')
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(urls_dict, json_file, indent=4)
    
    driver.quit()
    print(f"Webpage content saved: {txt_filename}")
    print(f"Images saved in: {os.path.join(domain_dir, 'images')}")
    print(f"Scripts saved in: {os.path.join(domain_dir, 'scripts')}")
    print(f"Extracted URLs saved in: {json_filename}")


# Example usage
if __name__=="__main__":
    # url_to_fetch = "https://en.wikipedia.org/wiki/Virat_Kohli"
    # url_to_fetch = "https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/02._Fundamental_Concepts_of_Quantum_Mechanics/Heisenberg's_Uncertainty_Principle#:~:text=non%2Dcommuting%20operators.-,Introduction,momentum%20is%20and%20vice%20versa."
    url_to_fetch = "https://www.geeksforgeeks.org/heisenberg-uncertainty-principle-definition-equation-significance/#:~:text=According%20to%20the%20Heisenberg%20Uncertainty%20Principle%2C%20there%20is%20a%20fundamental,is%20the%20reduced%20Planck%20constant."
    fetch_and_save_webpage_content(url_to_fetch)

