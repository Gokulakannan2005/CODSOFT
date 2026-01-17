from datetime import datetime


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello. I’m your virtual assistant. How can I help you today?"

    elif "how are you" in user_input:
        return "I’m functioning as expected. Thank you for asking."

    elif "your name" in user_input or "who are you" in user_input:
        return (
            "I’m a rule-based virtual assistant designed to respond "
            "to basic user queries using predefined rules."
        )

    elif "help" in user_input:
        return (
            "Here are a few things you can try:\n"
            "- Hello\n"
            "- What is your name?\n"
            "- How are you?\n"
            "- What is the time?\n"
            "- Exit"
        )

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current system time is {current_time}."

    elif user_input in ["bye", "exit", "quit"]:
        return "Conversation ended. Have a productive day."

    else:
        return (
            "I’m not able to respond to that yet.\n"
            "Please try typing 'help' to see available commands."
        )


def run_chatbot():
    print("Assistant: Initializing virtual assistant...")
    print("Assistant: Type 'help' to view available commands.")
    print("Assistant: Type 'exit' to end the session.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Assistant:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()
