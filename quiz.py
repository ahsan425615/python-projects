import requests

def get_questions(category, amount):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

def display_question(question):
    print("\n" + question['question'])
    answers = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(answers)
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")

def main():
    import random

    print("Welcome to the Quiz Game!")

    categories = {
        "General Knowledge": 9,
        "Science": 17,
        "History": 23,
        "Geography": 22
    }

    category = input("Choose a category:\n" + "\n".join([f"{key}: {value}" for key, value in categories.items()]) + "\n")
    amount = int(input("Enter the number of questions you want to answer: "))

    questions = get_questions(categories[category], amount)

    score = 0

    for question in questions:
        display_question(question)
        user_answer = int(input("Enter your answer (1/2/3/4): ")) - 1
        if question['incorrect_answers'][user_answer] == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['correct_answer'])

    print(f"\nQuiz complete! Your score: {score}/{amount}")

if __name__ == "__main__":
    main()
