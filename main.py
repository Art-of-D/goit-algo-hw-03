import shlex
from file_copy.file_generator import file_generator
from pathlib import Path
from file_copy.filler import Filler
from koch_snowdrop.snowdrop_painter import draw_koch_curve
from hanoi_temples.hanoi_temples import HanoiTemples
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

@input_error
def main():
    
    print("Welcome to the D&A bot!")
    print("Available commands: hello, copy, koch, hanoi, help, commands, close OR exit")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in ["copy", "1"]:
            parent_folder_path = Path("Temp")
            file_generator(parent_folder_path)
            filler = Filler("Temp")
            filler.recursive_copy()
        elif command in ["koch", "2"]:
            if len(args) != 1:
                print("Please enter a size of a Koch snowdrop.")
                continue
            draw_koch_curve_safe(args[0])
        elif command in ["hanoi", "3"]:
            if len(args) != 1:
                print("Please give a number of disk for hanoi temples")
            run_hanoi_safe(args[0])
        elif command in ["commands", "help", "command", "0"]:
            print("Available commands: hello, copy, koch, hanoi, help, commands, close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

@input_error
def draw_koch_curve_safe(order):
    try:
        n = int(order)
        if n < 1:
            raise ValueError()
        draw_koch_curve(n)
    except:
        raise ValueError("Please enter a number, more than 0")

@input_error
def run_hanoi_safe(n):
    try:
        n = int(n)
        if n < 1:
            raise ValueError()
        temples = HanoiTemples(n)
        temples.run()
    except:
        raise ValueError("Please enter a number, more than 0")

if __name__ == "__main__":
    main()