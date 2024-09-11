from ai_model import generate_ai_response
import json

def generate_soca_analysis(responses):
    # Improved prompt to explicitly ask for an analysis and not a repeat of the input data
    prompt = f'''The following are a JEE student's responses to a skill assessment questionnaire.
    Please analyze their responses and provide a detailed SOCA (Strengths, Opportunities, 
    Challenges, Action Plan) analysis. Be critical of the student's responses and provide 
    specific advice based on their answers, identifying strengths, areas of opportunity, 
    challenges they face, and an actionable plan for improvement.
    
    Student's responses:
    {json.dumps(responses, indent=2)}
    
    Provide the SOCA analysis as follows:
    
    Strengths:
    Opportunities:
    Challenges:
    Action Plan:

    DO NOT leave any of the four blank
    '''
    
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
