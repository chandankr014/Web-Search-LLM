"""
TAKE SINGLE QUERY AND PRODUCE N DIFFERENT QUERIES.
USE QUERY REFINING TECHNIQUES.
ALSO IT HAS INTENT CLASSIFIER FUNCTION
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from optimization.prompt import MASTER_PROMPT
import config

# VARIABLES -----------------------
API_KEY = config.API_KEY
# MODEL = config.MODEL


def invoke_intent(MODEL, query=None, t=0.4, log=True):

    model = ChatGoogleGenerativeAI(model=MODEL, temperature=t, api_key=API_KEY)
    prompt = MASTER_PROMPT(query)
    res = model.invoke(prompt)
    res = res.content # to avoid metadata

    if log==True:
        print("LOG: ", query, " ---> ", res)
        print("MODEL: ", MODEL)
        print("Temperature: ", t)

    return res


def invoke_prompt(MODEL, PROMPT=None, t=0.4):

    model = ChatGoogleGenerativeAI(model=MODEL, temperature=t, api_key=API_KEY)
    res = model.invoke(PROMPT)
    res = res.content 
    return res



# QUERY REFACTORING ------------------------------------
def refactor_query(query) -> str:
    PROMPT = f"""You are a helpful and accurate query refacor AI that do these series of operations alternately. \n
    Synonym Replacement: Automatically replacing less common words with their more familiar counterparts. \n
    Grammar Correction: Identifying and correcting grammatical errors in the query. \n
    Fuzzymatch: Based on context, find the best spelling for the mis-spelled words only. \n
    Simplification: Rephrasing complex sentences into simpler ones. And return the final query only. \n
    Query: **{query}** \n
    """
    op = invoke_prompt(PROMPT=PROMPT)
    return op


# QUERY REFINING ------------------------------------------------- modify more
def refine_query(query, intent=None) -> str:
    PROMPT = f"""You are a helpful and accurate assistant that refine the query. \n
    Consider the query and query intent. And refine the query to a appropriate query which carry the same semantic. \n
    Query: **{query}** \n
    Query's intent or category: {intent} \n
    """
    op = invoke_prompt(PROMPT=PROMPT)
    return op


# REPHRASE INTO N -------------------------------------------------
def rephrase_n_query(query, MODEL, N=4):
    PROMPT = f"""You are a helpful and accurate query rephraser. \n
    The goal is to rephrase the query into {N} different query which carry the same semantic. \n
    return the results as a LIST only nothing extra, for ex: ["item1", "item2", ... , "itemN"]. \n
    Query: **{query}** \n
    """
    op = invoke_prompt(MODEL, PROMPT=PROMPT)
    return op



# CALLING ---------------------------------------------
"""
query = "I am a computer science student, with data science specialization. i want to earn some side income, suggest me some ways and techniques."

intent = get_query_intent(query=query)

refactored = refactor_query(query=query)

refined = refine_query(query=query, intent=intent)

rephrased = rephrase_n_query(query=query)
rephrased_refactored = rephrase_n_query(query=refactored)

print(
    # "Intent: ", intent,
    "Refactored: ", refactored,
    "Refined: ", refined,
    "Rephresed: ", rephrased,
    "Rephresed_Refactored: ", rephrased_refactored
)

"""