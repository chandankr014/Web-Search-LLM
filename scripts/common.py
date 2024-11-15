"""
COMMON USED FUNCTIONS HERE
"""
import datetime
import json
import os
from urllib.parse import urlparse



# DUPLICATES -----------------------------------------------
def get_common_items(this_list):
    # input: 2D list
    # output: 1D list with common urls
    common_items = set(this_list[0])
    for sl in this_list[1:]:
        common_items.intersection_update(sl)
        if not common_items:
            break    
    return list(common_items)


def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def get_common_domain_urls(all_url):
    domain_dict = {}
    for url in all_url:
        domain = urlparse(url).netloc
        if domain in domain_dict:
            domain_dict[domain].append(url)
        else:
            domain_dict[domain] = [url]

    result_urls = []
    for urls in domain_dict.values():
        if len(urls) >= 2:
            for url in urls:
                if url not in result_urls:
                    result_urls.append(url)
    return result_urls


# READ JSON -----------------------------------------------
def read_json(fp):
    with open(fp, 'r') as f:
        data = json.load(f)
    return data


# SAVE JSON TO CURRENT DIR --------------------------------
def save_json_current_dir(data):

    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON Saved: {file_name}")


# SAVE JSON TO SPECIFIC DIR --------------------------------
def save_json(data, directory="answers"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".json"
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON Saved: {file_path}")


# SAVE TXT -------------------------------------------------------
def save_text(data, directory="answers"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".txt"
    file_path = os.path.join(directory, file_name)

    with open(file_path, 'w') as f:
        f.write(data)

    print(f"Text File Saved: {file_path}")


# CONVERT TO MARKDOWN --------------------------------------
def save_markdown(data, directory="Artifacts"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".md"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as f:
        f.write(data)

    print(f"MarkDown Saved: {file_path}")


def save_json(data, directory="Artifacts"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".json"
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"JSON Saved: {file_path}")



# SAVE URLs TO SPECIFIC DIR --------------------------------
def save_urls(urls=None, all_urls=None, directory="URLs"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".json"
    file_path = os.path.join(directory, file_name)
    
    data = {
        "urls": urls,
        "all_url": all_urls
    }
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON Saved: {file_path}")


def save_all_urls(urls=None, all_urls=None, directory="URLs"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    now = datetime.datetime.now()
    file_name = now.strftime("%y%m%d_%H%M%S") + ".json"
    file_path = os.path.join(directory, file_name)
    
    data = {
        "urls": urls,
        "all_url": all_urls
    }
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON Saved: {file_path}")
