#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and adds a port. """    
    port = int(input("Enter a port number: "))
    
    while True:
        print("Enter a command: ")
        cmd = input()
        if cmd == "exit":
            break
        else:
            