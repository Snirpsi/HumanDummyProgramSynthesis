#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that converts user input.
    while True:
        command = input("Enter a command: ")
        command = command.lower()
        if command == "exit":
            break
        if command == "help":
            print("\nCommands:")
            print("exit: Exits the program.")
            print("help: Displays this help message.")
        else:
            print("Invalid command.")

