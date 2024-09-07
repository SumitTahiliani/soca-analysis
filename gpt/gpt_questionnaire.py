def get_questionnaire_responses():
    responses = {}

    # Academic Questions (JEE Level)
    responses['physics_q1'] = input("Physics (MCQ): What is the SI unit of electric charge?\nA) Coulomb\nB) Ampere\nC) Volt\nD) Ohm\n")
    responses['physics_q2'] = input("Physics (MCQ): Which of the following quantities is a scalar?\nA) Velocity\nB) Acceleration\nC) Force\nD) Speed\n")
    
    responses['chemistry_q1'] = input("Chemistry (MCQ): Which element is the most electronegative?\nA) Oxygen\nB) Nitrogen\nC) Fluorine\nD) Chlorine\n")
    responses['chemistry_q2'] = input("Chemistry (MCQ): The chemical formula for table salt is:\nA) NaCl\nB) KCl\nC) NaF\nD) KBr\n")
    
    responses['math_q1'] = input("Mathematics (MCQ): What is the derivative of x^2?\nA) 1\nB) 2x\nC) x^3\nD) 3x^2\n")
    responses['math_q2'] = input("Mathematics (MCQ): What is the integral of 1/x?\nA) ln(x)\nB) x^2\nC) 1/x\nD) e^x\n")

    # Behavioral Questions
    responses['time_management'] = input("On a scale of 1-5, how do you rate your time management skills? (1 being poor, 5 being excellent)\n")
    responses['stress_management'] = input("On a scale of 1-5, how do you handle stress during exams? (1 being poor, 5 being excellent)\n")
    responses['study_techniques'] = input("How often do you revise topics after studying? (Rarely, Sometimes, Often, Always)\n")
    responses['problem_solving'] = input("How do you approach difficult problems in exams? (Give a brief answer)\n")

    return responses
