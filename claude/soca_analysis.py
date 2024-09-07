# soca_analysis.py

def generate_soca_analysis(processed_data, insights):
    strengths = [k for k, v in processed_data.items() if v >= 0.7]
    opportunities = [k for k, v in processed_data.items() if 0.4 <= v < 0.7]
    challenges = [k for k, v in processed_data.items() if v < 0.4]
    
    analysis = "SOCA Analysis:\n\n"
    analysis += "Strengths:\n"
    for strength in strengths:
        analysis += f"- {strength.replace('_', ' ').title()}: {processed_data[strength]:.2f}\n"
    
    analysis += "\nOpportunities:\n"
    for opportunity in opportunities:
        analysis += f"- Improve {opportunity.replace('_', ' ')}: {processed_data[opportunity]:.2f}\n"
    
    analysis += "\nChallenges:\n"
    for challenge in challenges:
        analysis += f"- {challenge.replace('_', ' ').title()}: {processed_data[challenge]:.2f}\n"
    
    analysis += "\nDetailed Insights:\n"
    analysis += f"Problem Solving Approach: {insights['problem_solving_insight']}\n\n"
    analysis += f"Stress Management: {insights['stress_management_insight']}\n\n"
    
    analysis += "Action Plan:\n"
    if 'subject_knowledge' in challenges:
        analysis += "1. Focus on strengthening core subject knowledge through intensive study.\n"
    if 'time_management' in challenges or 'time_management' in opportunities:
        analysis += "2. Develop a structured study schedule to improve time management.\n"
    if 'problem_solving' in challenges:
        analysis += "3. Practice more problem-solving exercises to enhance skills.\n"
    if 'stress_management' in challenges:
        analysis += "4. Learn and apply stress management techniques like meditation or deep breathing.\n"
    if 'study_techniques' in challenges or 'study_techniques' in opportunities:
        analysis += "5. Explore and adopt diverse study resources and techniques to improve learning efficiency.\n"
    
    return analysis