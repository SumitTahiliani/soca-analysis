# Function to generate SOCA analysis
from ai_model import generate_ai_response
import json

def generate_soca_analysis(responses):
    prompt = f'''Based on the following JEE student's responses, provide a SOCA 
    (Strengths, Opportunities, Challenges, Action Plan) analysis:
    \n\n{json.dumps(responses, indent=2)}. Be extremely critical of the student's
    answers, give specific targeted advice based on the questions being answered right
    or wrong\n\nSOCA Analysis:'''
    
    ai_response = generate_ai_response(prompt)
    
    # Extract SOCA components from AI response
    soca = {}
    current_section = ""
    for line in ai_response.split("\n"):
        if line.startswith("Strengths:"):
            current_section = "Strengths"
            soca[current_section] = []
        elif line.startswith("Opportunities:"):
            current_section = "Opportunities"
            soca[current_section] = []
        elif line.startswith("Challenges:"):
            current_section = "Challenges"
            soca[current_section] = []
        elif line.startswith("Action Plan:"):
            current_section = "Action Plan"
            soca[current_section] = []
        elif line.strip() and current_section:
            soca[current_section].append(line.strip())
    
    return soca