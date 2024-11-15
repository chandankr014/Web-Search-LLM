"""
input: rquery, response
output: scores, reasoning, prompt
"""

from evaluation.prompt import *


def CRITERIAS(query, response):
    prompt = relevance(query=query, response=response)
    return prompt

