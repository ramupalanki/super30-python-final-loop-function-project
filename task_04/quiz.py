"""Python Quiz Application."""

def get_questions():
    """Return the quiz questions and correct answers."""
    return [
        {"question": "What keyword defines a function in Python?", "answer": "def"},
        {"question": "Which symbol starts a comment in Python?", "answer": "#"},
        {"question": "Which loop is commonly used when the number of iterations is known?", "answer": "for"},
        {"question": "Which data type stores True or False?", "answer": "bool"},
        {"question": "What function displays output on the screen?", "answer": "print"},
    ]


def ask_question(question_number, question):
    """Display one question and return whether the answer is correct."""
    print(f"\nQuestion {question_number}: {question['question']}")
    answer = input("Your answer: ").strip().lower()
    if answer == question["answer"].lower():
        print("Correct!")
        return True
    print(f"Incorrect. Correct answer: {question['answer']}")
    return False


def calculate_percentage(score, total_questions):
    """Calculate quiz percentage."""
    return (score / total_questions) * 100


def main():
    """Run the quiz."""
    questions = get_questions()
    score = 0

    print("===== PYTHON QUIZ =====")
    for number, question in enumerate(questions, start=1):
        if ask_question(number, question):
            score += 1

    percentage = calculate_percentage(score, len(questions))
    print("\n===== FINAL RESULT =====")
    print(f"Final Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good effort!")
    else:
        print("Keep practicing!")


if __name__ == "__main__":
    main()
