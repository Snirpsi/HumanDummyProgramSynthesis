#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that requests user input.
    while True:
        print("Welcome to my little program!")
        print("Type 'quit' to quit.")
        command = input("Enter your command: ")
        if command == "quit":
            break
        else:
            print(command)

