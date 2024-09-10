from questionnaire import get_user_responses, questionnaire
from advanced_soca import generate_soca_analysis

def format_soca_analysis(soca_analysis):
    formatted_output = ""

    # Format each section
    formatted_output += "\nStrengths:\n"
    for strength in soca_analysis['Strengths']:
        formatted_output += f"- {strength}\n"

    formatted_output += "\nOpportunities:\n"
    for opportunity in soca_analysis['Opportunities']:
        formatted_output += f"- {opportunity}\n"

    formatted_output += "\nChallenges:\n"
    for challenge in soca_analysis['Challenges']:
        formatted_output += f"- {challenge}\n"

    formatted_output += "\nAction Plan:\n"
    for action in soca_analysis['Action Plan']:
        formatted_output += f"- {action}\n"

    return formatted_output

# Main function to run the skill assessment system
def run_skill_assessment():
    print("Welcome to the JEE Skill Assessment System!\n")
    responses = get_user_responses(questionnaire)
    soca_analysis = generate_soca_analysis(responses)
    output = format_soca_analysis(soca_analysis)
    print(output)
#     display_soca_analysis(soca_analysis)

# Run the skill assessment system
if __name__ == "__main__":
    run_skill_assessment()