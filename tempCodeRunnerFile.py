import kbcreal
kbcreal.__path__ = ['/home/runner/work/Good-Morning-Project/Good-Morning-Project/kbc']

import gms
gms.__annotations__ = {'greet': 'function'}

# 1. Greeting Function
def greet():
    gms.hour = gms.get_current_hour()  # Update hour in gms module
    greeting = gms.greet()
    print(greeting)
    return greeting

# 2. Function to check response
def should_start_quiz():
    response = input("Type 'start' to begin the quiz, or anything else to exit: ").strip().lower()
    if response == 'start':
        return True
    else:
        print("Quiz not started. Thank you!")
        return False

# 3. MAIN PROGRAM FLOW
def main():
    greet()  # First greet the user

    if should_start_quiz():  # Then ask about the quiz
        kbcreal.start_quiz()  # If yes, start the quiz

# 4. Run main function
main()
