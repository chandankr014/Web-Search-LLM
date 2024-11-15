"""
EXPORT VARIOUS OF PROMPTS FOR YOUR USE CASES.
"""

def PROMPT_ONE(question, context):
    PROMPT = f"""
        Please answer the following question in detail based on the provided context. 
        Include explanations of any core concepts mentioned in the context. 
        If there is any code provided, interpret it as well. 
        If the answer to the question is not covered in the context, state: "Answer is not available in the context."\n
        **Question:** {question} \n
        **Context:** {context} \n
    """
    return PROMPT


def PROMPT_TWO(question):
    PROMPT = f"""
        Given the question, provide a detailed breakdown of the answer. 
        Cover all core concepts, and explain them thoroughly.
        Highlight any relationships or dependencies between these concepts."\n
        **Question:**  {question}\n
    """
    return PROMPT

# PROMPT_TWO("your question here")