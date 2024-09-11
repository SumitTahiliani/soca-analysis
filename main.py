from questionnaire import get_user_responses, questionnaire
from advanced_soca import generate_soca_analysis

def format_soca_analysis(soca_analysis):
    formatted_output = ""

    # Loop through the analysis components and display each as a simple section
    for section, content in soca_analysis.items():
        formatted_output += f"\n{section}:\n"
        if content:
            for item in content:
                formatted_output += f"- {item}\n"
        else:
            formatted_output += "No data available.\n"
    
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