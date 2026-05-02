questions = [
    {"q": "What is 2+2?",  "a": "4"},
    {"q": "What is 3+2?",  "a": "5"},
    {"q": "What is 5+2?",  "a": "7"},
]

def ask_question(question, answer):
    user = input(question + " ")
    if user == answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! Answer was {answer}")
        return False

def run_quiz(questions):
    score = 0
    for q in questions:
        if ask_question(q["q"], q["a"]):
            score += 1
    print(f"You got {score} out of {len(questions)} correct!")

run_quiz(questions)