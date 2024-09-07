# main.py

import time
from questionnaire import run_questionnaire
from ai_model import process_answers
from gpt_soca_analysis import generate_soca_analysis

def main():
    print("Welcome to the JEE Student Skill Assessment System!")
    
    # Run questionnaire
    print("\nPlease answer the following questions:")
    answers = run_questionnaire()
    
    # Simulate processing time
    print("\nProcessing your answers. Please wait...")
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")
    
    # Process answers using AI model
    processed_data, insights = process_answers(answers)
    
    # Generate SOCA analysis
    soca_analysis = generate_soca_analysis(processed_data, insights)
    
    # Display results
    print(soca_analysis)

if __name__ == "__main__":
    main()