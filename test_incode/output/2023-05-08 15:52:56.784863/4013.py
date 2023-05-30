#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that converts user input.
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        elif command == "help":
            print("Enter a command: help")
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid command")

