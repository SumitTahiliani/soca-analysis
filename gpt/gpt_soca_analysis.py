def generate_soca_analysis(processed_data):
    soca_report = {
        "Strengths": [],
        "Opportunities": [],
        "Challenges": [],
        "Action Plan": []
    }

    # Analyze Physics, Chemistry, and Math answers
    for key, value in processed_data.items():
        if 'physics' in key or 'chemistry' in key or 'math' in key:
            if 'correct' in value.lower():  # Assuming the LLM response contains "correct" or "incorrect"
                soca_report['Strengths'].append(f"Strong in {key.split('_')[0]}")
            else:
                soca_report['Challenges'].append(f"Needs improvement in {key.split('_')[0]}")

    # Analyze Behavioral Responses
    if processed_data['time_management'] >= 4:
        soca_report['Strengths'].append("Good time management skills")
    else:
        soca_report['Opportunities'].append("Improve time management")

    if processed_data['stress_management'] >= 4:
        soca_report['Strengths'].append("Handles stress well")
    else:
        soca_report['Challenges'].append("Struggles with stress management")

    if 'often' in processed_data['study_techniques'].lower() or 'always' in processed_data['study_techniques'].lower():
        soca_report['Strengths'].append("Effective study techniques")
    else:
        soca_report['Opportunities'].append("Revise topics more frequently")

    soca_report['Action Plan'].append("Focus on areas marked under 'Challenges' and 'Opportunities'")

    return soca_report
