from flask import Flask, render_template, request, jsonify, url_for, redirect
import config
from ScrapGraph import main
import markdown
from scripts.ollama import ollama

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', models=config.MODELS)


@app.route('/ollama', methods=['GET'])
def ollama_route():
    query = request.args.get('query')
    MODEL = request.args.get('model')
    print("Config: ", MODEL)

    response_text = ollama(
        query=query,
        model=MODEL
    )
    res_md = markdown.markdown(response_text)
    return jsonify(res_md)


@app.route('/chat', methods=['POST'])
def chat():
    N = int(request.json.get('N', config.DEFAULT_N))
    TOP_N = int(request.json.get('TOP_N', config.DEFAULT_TOP_N))
    MODEL = request.json.get('model')
    MODE = request.json.get('headless_mode', config.DEFAULT_HEADLESS_MODE)
    query = request.json.get('message')
    
    ollama_models = ['qwen2.5-coder', 'llama3.1']
    if MODEL in ollama_models:
        return redirect(url_for('ollama_route', query=query, model=MODEL))

    print("Config: ", N, TOP_N, MODEL, MODE)
    # LLM Response
    response_text = main(
        query=query,
        N=N,
        TOP_N=TOP_N,
        MODEL=MODEL,
        API_KEY=config.API_KEY,
        HEADLESS_MODE=MODE,
        TEMP=config.TEMPERATURE
        )
    res_md = markdown.markdown(response_text)
    return jsonify(res_md)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
