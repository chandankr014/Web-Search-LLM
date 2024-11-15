from flask import Flask, render_template, request, jsonify
import config
from ScrapGraph import *
import markdown

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', models=config.MODELS)

@app.route('/chat', methods=['POST'])
def chat():
    N = int(request.json.get('N', config.DEFAULT_N))
    TOP_N = int(request.json.get('TOP_N', config.DEFAULT_TOP_N))
    MODEL = request.json.get('model')
    MODE = request.json.get('headless_mode', config.DEFAULT_HEADLESS_MODE)
    print("Config: ", N, TOP_N, MODEL, MODE)
    query = request.json.get('message')

    # LLM Response
    response_text = main(
        query=query,
        N=N,
        TOP_N=TOP_N,
        MODEL=MODEL,
        API_KEY=config.API_KEY,
        HEADLESS_MODE=MODE
        )
    res_md = markdown.markdown(response_text)
    return jsonify(res_md)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
