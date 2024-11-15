# MASTER-PROMPT --------------------------------------------------------------

def MASTER_PROMPT(query):
    PROMPT = f"""
        You are a helpful and accurate Query Intent Classification Model. \n
        help me to classify the intent from of the given query from the below Categories. \n
        NOTE: Just give the query name in a single word as given below. \n
        QUERY: **{query}** \n 
        CATEGORIES: 
            GENERAL 
            INFOMATIONAL 
            SUBJECT_SPECIFIC 
            EXPLANATION 
            DEFINITION 
            COMPARISON 
            DIFFERENTIATION
            HOW_TO 
            RECOMMENDATION 
            EXAMPLE 
            HISTORICAL 
            PROBLEM_SOLVING 
            CONCEPTUAL 
            RESOURCE 
            RESEARCH
            FOLLOW_UP 
            GREETING 
            FEEDBACK 
            NAVIGATIONAL \n
        If query is not suitable or accurate for any category just return "MISCELLANEOUS". \n
    """
    return PROMPT



# PROMPTS --------------------------------------------------------------

# Required special case definition for follow-up to perform chaining.
def FOLLOW_UP(context, query):
    PROMPT = f"""
        Based on what we've discussed about **{context}**, \n
        could you provide more details or expand on **{query}**? \n
    """
    return PROMPT


def GENERAL(query): # GENERAL==MISCELLANEOUS
    PROMPT = f"""
        Could you give me an overview of **{query}**\n 
        I’m interested in understanding the basic aspects and main ideas related to it.\n
    """
    return PROMPT


def INFORMATIONAL(query):
    PROMPT = f"""
        I need information about **{query}**.\n
        Can you provide details on its key components, background, and any important facts or figures.\n
        be qualitative as well as quantitative.\n
    """
    return PROMPT


def SUBJECT_SPECIFIC(query):
    PROMPT = f"""
        Could you dive into **{query}** and explain its main concepts or details? \n
        I'm interested in learning more about how it works or what it involves. \n
    """
    return PROMPT


def NAVIGATIONAL(query):
    PROMPT = f"""
        Can you help me find the section or information related to **{query}**? \n
        I'm trying to locate specific details within a larger document or resource. \n
    """
    return PROMPT


def GREETING(query):
    PROMPT = f"""
        Hi! How are you doing today? \n
        I'm excited to learn more about **{query}** and would appreciate your guidance. \n
    """
    return PROMPT


def EXAMPLE(query):
    PROMPT = f"""
        Please provide an example for the following query: **{query}** \n
    """
    return PROMPT


def DEFINITION(query):
    PROMPT = f"""
        What does **{query}** mean? Please provide a clear and concise definition, \n
        and if possible, include an example to illustrate its usage.\n
    """
    return PROMPT


def EXPLANATION(query):
    PROMPT = f"""
        Can you explain about **{query}**?\n
        I'd like a detailed breakdown of core concepts, functioning, including any relevant factors or steps involved.\n
    """
    return PROMPT


def FEEDBACK(query):
    PROMPT = f"""
        I recently learned about **{query}**, and I'd love to get your feedback on it. \n
        Do you think I'm on the right track, or is there something I should consider. \n
    """
    return PROMPT


def COMPARISON(query):
    PROMPT = f"""
        Comparison for **{query}**, highlighting their similarities and differences? \n
        I'm particularly interested in core similarity and functions. \n
    """
    return PROMPT


def DIFFERENTIATION(query):
    PROMPT = f"""
        Differentiation for **{query}**, highlighting their similarities and differences? \n
        I'm particularly interested in core differences and functions. \n
    """
    return PROMPT


def HOW_TO(query):
    PROMPT = f"""
        Could you guide me through the steps to **{query}**? \n
        A step-by-step explanation would be very helpful. \n
    """
    return PROMPT


def RECOMMENDATION(query):
    PROMPT = f"""
        What would you recommend for **{query}**? \n
        I'm looking for suggestions that is helpful and infomative. \n
        Add examples if needed \n
    """
    return PROMPT


def CONCEPTUAL(query):
    PROMPT = f"""
        "What is the underlying concept or theory behind **{query}**? \n
        Please break down the core principles and how they interconnect.

    """
    return PROMPT


def PROBLEM_SOLVING(query):
    PROMPT = f"""
        I'm facing a challenge with **{query}**. \n
        Could you suggest potential solutions or ways to approach and resolve this issue?
    """
    return PROMPT


def HISTORIC(query):
    PROMPT = f"""
        Can you tell me about the history of **{query}**? \n
        I'd like to understand its origins, key milestones, and significance.
    """
    return PROMPT


def RESOURCE(query):
    PROMPT = f"""
        Where can I find reliable resources or references for **{query}**? \n
        I'm looking for books, articles, or online materials that provide in-depth information.
    """
    return PROMPT


def RESEARCH(query):
    PROMPT = f"""
        You are a highly skilled Research Assistant AI. Your task is to conduct thorough research on the topic: **{query}**. \n
        Your research should include a comprehensive analysis, combining both qualitative and quantitative methods as needed. \n
        Ensure that your findings are well-organized, coherent, and provide a clear, insightful conclusion. \n
        If applicable, include relevant data, trends, or statistics to support your analysis. \n
        Your final response should be concise yet detailed, offering valuable insights and actionable recommendations.
    """
    return PROMPT


def REVERSE_ENGINEERING(response):
    PROMPT = f"""
        You are a Text Analysis AI specialized in reverse engineering responses to uncover their underlying questions or prompts. \n
        Given the following text: **{response}**, \n
        your task is to deduce the original question or prompt that likely led to this response. \n
        Carefully analyze the content, context, and any implied information to reconstruct the most accurate and relevant question. \n
        Ensure your final output is precise, clearly formulated, and directly aligns with the content provided. \n
    """
    return PROMPT

