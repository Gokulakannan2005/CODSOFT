import time
import sys
from datetime import datetime
import msvcrt


def clear_keyboard_buffer():
    """Remove any pending key presses from the buffer."""
    while msvcrt.kbhit():
        msvcrt.getch()


def typewriter_effect(text, delay=0.04):
    """
    Prints text one character at a time.
    Press Enter during animation to instantly display the remaining text.
    """
    clear_keyboard_buffer()  # 🔑 critical fix

    i = 0
    while i < len(text):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':  # Enter key
                sys.stdout.write(text[i:])
                sys.stdout.flush()
                break

        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
        i += 1

    print()


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello. I’m your virtual assistant. How can I help you today?"

    elif "how are you" in user_input:
        return "I’m functioning as expected. Thank you for checking."

    elif "your name" in user_input or "who are you" in user_input:
        return (
            "I’m a rule-based chatbot designed to respond to user inputs "
            "using predefined logical conditions."
        )

    elif "help" in user_input:
        return (
            "Available commands:\n"
            "- Hello\n"
            "- What is your name?\n"
            "- What is the time?\n"
            "- Exit"
        )

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current system time is {current_time}."

    elif user_input in ["bye", "exit", "quit"]:
        return "Conversation terminated. Have a productive day."

    else:
        return (
            "I’m not able to respond to that yet.\n"
            "Type 'help' to see available commands."
        )


def run_chatbot():
    typewriter_effect("Initializing assistant...")
    typewriter_effect("System ready.")
    typewriter_effect("Type 'help' to view available commands.")
    typewriter_effect("Type 'exit' to end the session.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        typewriter_effect(response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()
