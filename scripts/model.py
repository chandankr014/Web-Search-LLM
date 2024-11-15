from langchain_google_genai import ChatGoogleGenerativeAI
from scripts.common import read_json
from scripts.prompt import PROMPT_ONE, PROMPT_TWO
import config


API_KEY = config.API_KEY
MODEL = config.MODEL

# INVOKE
def invoke_query(MODEL=MODEL, question=None, context=None, t=0.4):

    model = ChatGoogleGenerativeAI(model=MODEL, temperature=t, api_key=API_KEY)
    prompt = PROMPT_TWO(question)
    res = model.invoke(prompt)
    return res


# INVOKE WITH PROMPT ONLY
def invoke_prompt(MODEL=MODEL, PROMPT=None, t=0.4):

    model = ChatGoogleGenerativeAI(model=MODEL, temperature=t, api_key=API_KEY)
    res = model.invoke(PROMPT)
    res = res.content 
    return res


# INVOKE WITH FILEPATH
def invoke_filepath(MODEL=MODEL, question=None, filepath=None, t=0.4):
    
    data = read_json(filepath)

    answers = data.get('answers', [])
    combined_answers = ' '.join(answers)

    prompt = PROMPT_ONE(question, combined_answers)
    model = ChatGoogleGenerativeAI(model=MODEL, temperature=t, api_key=API_KEY)
    res = model.invoke(prompt)
    return res

