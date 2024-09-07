from gpt_llm_integration import analyze_response

def process_responses(responses):
    processed_data = {}

    # Process Academic Questions
    for question, response in responses.items():
        if 'physics' in question or 'chemistry' in question or 'math' in question:
            # Send to LLM for analysis
            processed_data[question] = analyze_response(response)

    # Process Behavioral Questions
    processed_data['time_management'] = int(responses['time_management'])
    processed_data['stress_management'] = int(responses['stress_management'])
    processed_data['study_techniques'] = responses['study_techniques']
    processed_data['problem_solving'] = analyze_response(responses['problem_solving'])

    return processed_data
