import shlex


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decorators.error_handler import input_error

def parse_input(user_input):
    """
    Parse the user's input into a command and arguments.

    Args:
        user_input (str): The user's input.

    Returns:
        tuple: A tuple of the command and arguments. If the user entered no command, returns ("commands", []).
    """
    if not user_input:
        print("Please enter a command.")
        return "commands", []

    try:
        tokens = shlex.split(user_input)
        cmd = tokens[0].strip().lower() if tokens else "commands"
        args = tokens[1:] if len(tokens) > 1 else []
        return cmd, args
    except ValueError as e:
        print(f"Error parsing input: {e}")
        return "commands", []



def main():
    
    print("Welcome to the D&A bot!")
    print("Available commands: hello, application, palindrom, check, help, commands, close OR exit")
    print("!Note! If you want to use an argument that contain more than one word, enclose it in quotes.")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in ["application", "1"]:
            application = Application()
            application.run()
        elif command in ["palindrom", "2"]:
            if len(args) != 1:
                print("Please enter a word to check as a palindrome.")
                continue
            palindrom = Palindrom()
            print(palindrom.run(args[0]))
        elif command in ["check", "3"]:
            checker = ParenthesisChecker()
            print(checker.check(args[0]))
        elif command in ["commands", "help", "command", "0"]:
            print("Available commands: hello, application, palindrom, check, help, commands, close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()