# ai_model.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_insight(prompt, answer):
    # Combine prompt and answer
    input_text = f"{prompt}\nStudent's answer: {answer}\nAnalysis:"
    
    # Tokenize input
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    
    # Generate response
    output = model.generate(
        input_ids, 
        max_length=150, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2, 
        temperature=0.7
    )
    
    # Decode and return the generated text
    return tokenizer.decode(output[0], skip_special_tokens=True)

def process_answers(answers):
    processed_data = {
        "subject_knowledge": 0,
        "time_management": 0,
        "problem_solving": 0,
        "stress_management": 0,
        "study_techniques": 0
    }
    
    # Process multiple choice questions
    if answers['P1'] == 0:  # Correct answer for P1
        processed_data['subject_knowledge'] += 1
    if answers['C1'] == 1:  # Correct answer for C1
        processed_data['subject_knowledge'] += 1
    if answers['M1'] == 1:  # Correct answer for M1
        processed_data['subject_knowledge'] += 1
    
    # Process scale question
    processed_data['time_management'] = answers['TM1'] / 5  # Normalize to 0-1 scale
    
    # Process short answer questions using GPT-2
    problem_solving_insight = generate_insight(
        "Analyze the following approach to problem-solving in the context of JEE preparation:",
        answers['PS1']
    )
    processed_data['problem_solving'] = analyze_insight(problem_solving_insight)
    
    stress_management_insight = generate_insight(
        "Evaluate the following stress management technique for JEE exam preparation:",
        answers['SM1']
    )
    processed_data['stress_management'] = analyze_insight(stress_management_insight)
    
    # Process study techniques (assuming more resources is better)
    if isinstance(answers['ST1'], list):
        processed_data['study_techniques'] = len(answers['ST1']) / 4  # 4 is the total number of options
    else:
        processed_data['study_techniques'] = 1 / 4
    
    return processed_data, {
        'problem_solving_insight': problem_solving_insight,
        'stress_management_insight': stress_management_insight
    }

def analyze_insight(insight):
    # Simple sentiment analysis on the generated insight
    positive_keywords = ['effective', 'good', 'excellent', 'efficient', 'beneficial']
    negative_keywords = ['ineffective', 'poor', 'inadequate', 'inefficient', 'harmful']
    
    score = 0.5  # Start with a neutral score
    for word in positive_keywords:
        if word in insight.lower():
            score += 0.1
    for word in negative_keywords:
        if word in insight.lower():
            score -= 0.1
    
    return max(0, min(1, score))  # Ensure score is between 0 and 1