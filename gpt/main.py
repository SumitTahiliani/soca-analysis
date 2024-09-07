from gpt_questionnaire import get_questionnaire_responses
from gpt_process_responses import process_responses
from gpt_soca_analysis import generate_soca_analysis
import json

def save_responses_to_file(responses, filename="responses.json"):
    with open(filename, 'w') as f:
        json.dump(responses, f, indent=4)

def load_responses_from_file(filename="responses.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    # Step 1: Get the questionnaire responses
    responses = get_questionnaire_responses()

    # Step 2: Save the responses to a file
    save_responses_to_file(responses)

    # Optional: Load responses from the file if needed
    responses_from_file = load_responses_from_file()

    # Step 3: Process the responses
    processed_data = process_responses(responses_from_file)

    # Step 4: Generate SOCA analysis
    soca_report = generate_soca_analysis(processed_data)

    # Output the final SOCA report
    print("SOCA Analysis Report:")
    print(soca_report)

if __name__ == "__main__":
    main()
