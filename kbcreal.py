def start_quiz():
    questions = {
        "What is the capital of India": "Delhi",
        "What is the National Bird of India": "Peacock",
        "What is the National Animal of India": "Tiger",
        "How many states are there in India": "28",
    }

    level = [1000, 2000, 4000, 8000, 16000, 32000, 64000,
             128000, 256000, 500000, 1000000, 2500000, 5000000, 10000000]
    
    Options = [
        ["Delhi", "Kolkata", "Mumbai", "Chennai"],
        ["Pigeon", "Crow", "humming bird", "Peacock"],
        ["Elephant", "Lion", "Tiger", "Liger"],
        ["9", "28", "31", "23"],
    ]

    i = 0
    for index, (question, answer) in enumerate(questions.items()):
        print(f"\nQuestion for ₹{level[i]}:")
        user_ans = input(f"{question}?\nOptions: {Options[i]} \nYour Answer: ")
        if user_ans == answer:
            print("✅ Correct!")
            i += 1
            if i == len(questions):
                print("🎉 Congratulations! You won ₹", level[i-1])
        else:
            print("❌ Incorrect! You are out.")
            break

    if i > 0:
        print("You have won ₹", level[i-1])
    else:
        print("Better luck next time!")

# To start the quiz:
start_quiz()

