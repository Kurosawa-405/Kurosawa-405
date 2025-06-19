# Kaun Banega Crorepati Quiz Game

questions = {
    "What is the capital of India?": "Delhi",
    "What is the National Bird of India?": "Peacock",
    "What is the National Animal of India?": "Tiger",
    "How many states are there in India?": "28",
}

levels = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 500000, 1000000, 2500000, 5000000, 10000000]
options = [
    ["Delhi", "Kolkata", "Mumbai", "Chennai"],
    ["Pigeon", "Crow", "Humming Bird", "Peacock"],
    ["Elephant", "Lion", "Tiger", "Liger"],
    ["9", "28", "31", "23"],
]
def start_game():
    print("Welcome to Kaun Banega Crorepati!")
    score = 0
    for i, (question, correct_answer) in enumerate(questions.items()):
        print(f"\nQuestion for ₹{levels[i]}: {question}")
    for idx, option in enumerate(options[i]):
        print(f"{idx + 1}. {option}")

    answer = input("Your answer (type the option number): ")
    
    # Ensure the answer is within the valid range
    if answer.isdigit() and 1 <= int(answer) <= len(options[i]):
        selected_option = options[i][int(answer) - 1]
        if selected_option == correct_answer:
            score += levels[i]
            print(f"Correct! Your score is now ₹{score}.")
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}.")
            break
    else:
        print("Invalid option selected! Please choose a valid number.")
        break

print(f"Game over! Your final score is ₹{score}.")
