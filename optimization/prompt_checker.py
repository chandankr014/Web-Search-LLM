from optimization.query import refactor_query, invoke_intent
from optimization.switch import Switcher


# QUESTIONS ---------------------------------------------
que = [
    # "I am a computer science student, with data science specialization. i want to earn some side income, suggest me some ways and techniques."
]

switcher = Switcher()

for q in que:
    q = refactor_query(query=q)
    intent = invoke_intent(question=q)
    result = switcher.Switch(intent, q)  
    print(result)
