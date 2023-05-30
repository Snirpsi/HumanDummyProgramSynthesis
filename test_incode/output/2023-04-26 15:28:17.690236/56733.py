#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or removes all ports. """    
    while True:
        print("Type 'exit' to exit.")
        command = input("Command: ")
        if command == "exit":
            break
        elif command == "fruit":
            print("Fruit added")
        elif command == "port":
            print("Port removed")
        else:
            print("Unknown command")
        
