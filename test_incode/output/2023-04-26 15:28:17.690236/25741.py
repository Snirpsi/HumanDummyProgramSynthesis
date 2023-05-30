#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports and calculates user input. """    
    while True:
        port = int(input("Enter a port: "))
        if port > 0 and port <= 65535:
            ports.append(port)
        else:
            print("Invalid port number")
    
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        else:
            command = command.split()
            command = command[1]
            if command == "ping":
                ping()
            elif command == "help":
                help()
            else:
                print("Invalid command")
    
    ports.sort()
    
    print("Ports:", ports)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
