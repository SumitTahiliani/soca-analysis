# Define the questionnaire
questionnaire = {
    "Physics": [
        {"question": "A ball is thrown vertically upward with an initial velocity of 20 m/s. Neglecting air resistance, what is its maximum height?", "type": "short_answer"},
        {"question": "Which of the following is NOT a type of electromagnetic radiation? A) X-rays B) Gamma rays C) Alpha particles D) Microwaves", "type": "multiple_choice"},
        {"question": "Explain the concept of work-energy theorem in your own words.", "type": "short_answer"}
    ],
    "Chemistry": [
        {"question": "Balance the following chemical equation: Fe + O2 → Fe2O3", "type": "short_answer"},
        {"question": "Which of the following is an example of a covalent compound? A) NaCl B) H2O C) CaO D) KCl", "type": "multiple_choice"},
        {"question": "Describe the difference between SN1 and SN2 reactions in organic chemistry.", "type": "short_answer"}
    ],
    "Mathematics": [
        {"question": "Solve the equation: log2(x) + log2(x+1) = 3", "type": "short_answer"},
        {"question": "What is the derivative of f(x) = x^3 - 2x^2 + 4x - 1?", "type": "short_answer"},
        {"question": "In how many ways can 5 different books be arranged on a shelf?", "type": "short_answer"}
    ],
    "Time Management": [
        {"question": "On a scale of 1-10, how well do you manage your study time?", "type": "scale"},
        {"question": "How many hours do you typically study per day?", "type": "short_answer"},
        {"question": "What is your preferred method for scheduling your study sessions?", "type": "short_answer"}
    ],
    "Problem Solving": [
        {"question": "Describe your approach to solving a complex problem you've never encountered before.", "type": "short_answer"},
        {"question": "On a scale of 1-10, how confident are you in your problem-solving abilities?", "type": "scale"},
        {"question": "What resources do you typically use when stuck on a problem?", "type": "short_answer"}
    ],
    "Stress Management": [
        {"question": "On a scale of 1-10, how would you rate your current stress level regarding JEE preparation?", "type": "scale"},
        {"question": "What techniques do you use to manage stress during exam preparation?", "type": "short_answer"},
        {"question": "How often do you take breaks during your study sessions?", "type": "short_answer"}
    ],
    "Study Techniques": [
        {"question": "What study materials do you primarily use for JEE preparation?", "type": "short_answer"},
        {"question": "Do you prefer studying alone or in a group? Why?", "type": "short_answer"},
        {"question": "On a scale of 1-10, how effective do you find your current study techniques?", "type": "scale"}
    ]
}

# Function to get user responses
def get_user_responses(questionnaire):
    responses = {}
    for category, questions in questionnaire.items():
        responses[category] = []
        print(f"\n{category} Questions:")
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            if q['type'] == 'multiple_choice':
                response = input("Enter your choice (A/B/C/D): ").strip().upper()
            elif q['type'] == 'scale':
                response = int(input("Enter a number between 1-10: "))
            else:
                response = input("Enter your answer: ").strip()
            responses[category].append(response)
    return responses