"""
This is a switcher for switching the PROMPT.
Input: str, str
Output: str
"""

from optimization.prompt import *

class Switcher:

    def Informational(self, query):
        prompt = INFORMATIONAL(query=query)
        return prompt

    def Subject_Specific(self, query):
        prompt = SUBJECT_SPECIFIC(query=query)
        return prompt

    def Explanation(self, query):
        prompt = EXPLANATION(query=query)
        return prompt

    def Differentiation(self, query):
        prompt = DIFFERENTIATION(query=query)
        return prompt

    def Comparison(self, query):
        prompt = COMPARISON(query=query)
        return prompt

    def How_to(self, query):
        prompt = HOW_TO(query=query)
        return prompt

    def Recommendation(self, query):
        prompt = RECOMMENDATION(query=query)
        return prompt

    def Example(self, query):
        prompt = EXAMPLE(query=query)
        return prompt

    def Definition(self, query):
        prompt = DEFINITION(query=query)
        return prompt

    def Conceptual(self, query):
        prompt = CONCEPTUAL(query=query)
        return prompt

    def Historic(self, query):
        prompt = HISTORIC(query=query)
        return prompt
    
    def Problem_solving(self, query):
        prompt = PROBLEM_SOLVING(query=query)
        return prompt

    def Resource(self, query):
        prompt = RESOURCE(query=query)
        return prompt

    def Follow_up(self, query):
        prompt = FOLLOW_UP(query=query)
        return prompt

    def Greeting(self, query):
        prompt = GREETING(query=query)
        return prompt

    def Feedback(self, query):
        prompt = FEEDBACK(query=query)
        return prompt

    def Navigational(self, query):
        prompt = NAVIGATIONAL(query=query)
        return prompt

    def Research(self, query):
        prompt = RESEARCH(query=query)
        return prompt

    # Default method
    def General(self, query):
        prompt = GENERAL(query=query)
        return prompt


    # SWITCHING ---------------------------------
    def Switch(self, intent, query):
        # Mapping INPUT : OUTPUT
        method_mapping = {
            "INFORMATIONAL": self.Informational,
            "SUBJECT_SPECIFIC": self.Subject_Specific,
            "EXPLANATION": self.Explanation,
            "DIFFERENTIATION": self.Differentiation,
            "COMPARISON": self.Comparison,
            "HOW_TO": self.How_to,
            "RECOMMENDATION": self.Recommendation,
            "EXAMPLE": self.Example,
            "DEFINITION": self.Definition,
            "CONCEPTUAL": self.Conceptual,
            "HISTORIC": self.Historic,
            "PROBLEM_SOLVING": self.Problem_solving,
            "RESOURCE": self.Resource,
            "FOLLOW_UP": self.Follow_up,
            "GREETING": self.Greeting,
            "FEEDBACK": self.Feedback,
            "NAVIGATIONAL": self.Navigational,
            "RESEARCH": self.Research,
            "GENERAL": self.General,
            "MISCELLANEOUS": self.General
        }

        # Determine the method to call based on the case
        # Call the method with the provided arguments and return the result
        method = method_mapping.get(intent, self.General)
        prompt = method(query)
        return prompt


# # CALLING --------------------------------------------
# switcher = Switcher()
