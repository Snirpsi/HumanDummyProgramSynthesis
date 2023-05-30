#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or converts user input. """    
    while True:
        try:
            command = input("Enter a command: ")
            command = command.lower()
            if command == "quit":
                exit()
            elif command == "exit":
                exit()
            elif command == "help":
                print("Commands:")
                print("  quit   Quit the program")
                print("  exit  Exit the program")
                print("  help  Display this help")
            else:
                command = command.split()
                command = command[0]
                command = command[1:]
                if command == "convert":
                    convert(command[1:])
                else:
                    print("Unknown command")
        except KeyboardInterrupt:
            print("\nProgram terminated")
            break
