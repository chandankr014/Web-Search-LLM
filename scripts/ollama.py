import requests
import markdown
import json
import subprocess
import threading
import time


server_thread_running = False  


def __initialize_ollama__():
    print("##------------------ initializing ollama server ------------------##")
    process = subprocess.Popen("ollama serve", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print("Output:", stdout)
    print("Error:", stderr)
    print("Exit Code:", process.returncode)


def ollama_model(query, model="qwen2.5-coder", prompt="You are a helpful assistant"):
    global server_thread_running
    if not server_thread_running:
        server_thread_running = True
        server_thread = threading.Thread(target=__initialize_ollama__, daemon=True)
        server_thread.start()
        print("##------------------ server is now running ------------------##")
        time.sleep(2)
    else:
        print("##------------------ server already running ------------------##")

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
    }

    response = requests.post(url, json=payload)
    return response


def response_handler(response):
    lines = response.text.splitlines()
    full_response = ""

    for line in lines:
        json_line = json.loads(line) 
        content = json_line["message"]["content"] 
        full_response += content 

    res_md = markdown.markdown(full_response)
    return res_md

# calling
def ollama(query, model):
    # return the response in markdown format
    return response_handler(
        ollama_model(
            query=query,
            model=model
        )
    )
