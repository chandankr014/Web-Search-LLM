from optimization.models import invoke_prompt

age_ranges = ["under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 and above"]

user_input = "I am a computer science student, with data science specialization. i want to earn some side income, suggest me some ways and techniques."

prompt = f"""
    Given the query: '{user_input}', 
    which age range does the speaker likely belong to? 
    Options: {', '.join(age_ranges)}. \n
    Also show how confident/accurate (Score: 0-10) your answer is? 
    Return the score for all. \n 
"""

response = invoke_prompt(PROMPT=prompt)
print(f"Predicted Age Range: {response}")
