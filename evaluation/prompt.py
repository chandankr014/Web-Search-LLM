

def evaluation_prompt(query=None, response=None):
    
    PROMPT = f"""
        Evaluate the response based on the following criteria and provide a score from 1 to 5, where 1 is poor and 5 is excellent:

        QUERY: **{query}** \n
        RESPONSE: \n**{response}** \n

        Relevance: Does the response directly address the query?
        Score:
        Correctness: Is the information accurate and verifiable?
        Score:
        Completeness: Does the response cover all aspects of the query?
        Score:
        Conciseness: Is the response clear and to the point without unnecessary elaboration?
        Score:
        Coherence: Is the response logically structured and easy to follow?
        Score:
        Fluency: Is the response grammatically correct and well-written?
        Score:
        Overall Evaluation: Summarize the overall quality of the response, highlighting the most critical areas for improvement.
    """
    return PROMPT


def relevance(query=None, response=None):
    PROMPT = f"""
        Does the response directly address the user's query? 
        Identify any parts of the response that are unrelated or stray from the core question.
        \nQuery: **{query}** \nResponse: **{response}**
    """
    return PROMPT


def correctness(query=None, response=None):
    PROMPT = f"""
        Is the information in the response factually accurate and verifiable? 
        Identify any inaccuracies or misleading content.
        \nQuery: **{query}** \nResponse: **{response}**
    """
    return PROMPT


def completeness(query=None, response=None):
    PROMPT = f"""
        Does the response fully cover the main query and any sub-questions? 
        Highlight any missing information or areas that need further elaboration.
        \nQuery: **{query}** \nResponse: **{response}**
    """
    return PROMPT


def conciseness(query=None, response=None):
    PROMPT = f"""
        Is the response clear and concise, avoiding unnecessary elaboration? 
        Point out any redundant or overly verbose parts.
        \nQuery: **{query}** \nResponse: **{response}**
    """
    return PROMPT


def coherence(query=None, response=None):
    PROMPT = f"""
        Is the response logically structured and easy to follow? 
        Identify any parts where the flow of ideas is unclear or disjointed.
        \nQuery: **{query}** \nResponse: **{response}**
    """
    return PROMPT


def fluency(query=None, response=None):
    
    PROMPT = f"""
        Is the response grammatically correct and well-written for the query, 
        with a natural flow? Highlight any grammatical errors or awkward phrasing. \n
        Query: **{query}** \n
        Response: **{response}** \n
    """
    return PROMPT


