# questionnaire.py

questions = [
    {
        "id": "P1",
        "text": "Which of the following best describes Newton's First Law of Motion?",
        "type": "multiple_choice",
        "options": [
            "An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.",
            "Force equals mass times acceleration.",
            "For every action, there is an equal and opposite reaction.",
            "The acceleration of an object as produced by a net force is directly proportional to the magnitude of the net force."
        ],
        "correct_answer": 0
    },
    {
        "id": "C1",
        "text": "What is the pH of a neutral solution at 25°C?",
        "type": "multiple_choice",
        "options": ["0", "7", "14", "1"],
        "correct_answer": 1
    },
    {
        "id": "M1",
        "text": "What is the derivative of f(x) = x^2 with respect to x?",
        "type": "multiple_choice",
        "options": ["x^2", "2x", "2", "x"],
        "correct_answer": 1
    },
    {
        "id": "TM1",
        "text": "On a scale of 1-5, how well do you manage your study time?",
        "type": "scale",
        "min": 1,
        "max": 5
    },
    {
        "id": "PS1",
        "text": "When faced with a difficult problem, what is your usual approach?",
        "type": "short_answer"
    },
    {
        "id": "SM1",
        "text": "How do you typically handle stress during exam preparation?",
        "type": "short_answer"
    },
    {
        "id": "ST1",
        "text": "What study resources do you primarily use for JEE preparation?",
        "type": "multiple_choice",
        "options": ["Textbooks", "Online courses", "Coaching classes", "Self-study materials"],
        "multiple": True
    }
]

def display_question(question):
    print(f"\nQuestion: {question['text']}")
    if question['type'] == 'multiple_choice':
        for i, option in enumerate(question['options']):
            print(f"  {i+1}. {option}")
    elif question['type'] == 'scale':
        print(f"  (Enter a number between {question['min']} and {question['max']})")

def get_answer(question):
    if question['type'] == 'multiple_choice':
        while True:
            try:
                answer = int(input("Your answer (enter the number): ")) - 1
                if 0 <= answer < len(question['options']):
                    return answer
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    elif question['type'] == 'scale':
        while True:
            try:
                answer = int(input("Your answer: "))
                if question['min'] <= answer <= question['max']:
                    return answer
                else:
                    print(f"Please enter a number between {question['min']} and {question['max']}.")
            except ValueError:
                print("Please enter a valid number.")
    elif question['type'] == 'short_answer':
        return input("Your answer: ")

def run_questionnaire():
    answers = {}
    for question in questions:
        display_question(question)
        answers[question['id']] = get_answer(question)
    return answers
