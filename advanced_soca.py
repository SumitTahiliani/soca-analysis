from ai_model import generate_ai_response
import json

def generate_soca_analysis(responses):
    # Updated prompt to explicitly request each SOCA component clearly
    prompt = f'''Based on the following JEE student's responses, provide a detailed SOCA 
    (Strengths, Opportunities, Challenges, Action Plan) analysis. Each section should be 
    clearly separated and labeled as follows:
    
    Strengths:
    Opportunities:
    Challenges:
    Action Plan:
    
    Student's responses:
    \n\n{json.dumps(responses, indent=2)}.'''
    
    # Generate the AI response
    ai_responses = generate_ai_response(prompt)
    ai_response = ai_responses[0]
    
    # Separate SOCA components
    soca = {"Strengths": [], "Opportunities": [], "Challenges": [], "Action Plan": []}
    current_section = None
    
    # Simplify parsing by looking for keywords directly
    for line in ai_response.split("\n"):
        line = line.strip()
        if "Strengths:" in line:
            current_section = "Strengths"
        elif "Opportunities:" in line:
            current_section = "Opportunities"
        elif "Challenges:" in line:
            current_section = "Challenges"
        elif "Action Plan:" in line:
            current_section = "Action Plan"
        elif line and current_section:
            soca[current_section].append(line)
    
    return soca
