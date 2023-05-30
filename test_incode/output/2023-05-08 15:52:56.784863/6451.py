#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that converts user input.
    while True:
        command = input("Enter a command: ")
        if command == 'exit':
            break
        elif command == 'help':
            print("Commands:")
            print("exit: exits the program")
            print("help: prints this message")
        else:
            print("Unknown command: " + command)

