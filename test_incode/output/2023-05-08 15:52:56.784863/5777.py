#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    
    #The port number must be greater than 0.
    if port <= 0:
        print("Port number must be greater than 0.")
        exit(1)
    
    #The port number must be less than 65535.
    if port > 65535:
        print("Port number must be less than 65535.")
        exit(1)
    
    #The port number must be greater than 0 and less than 65535.
    if port > 0 and port < 65535:
        print("Port number must be greater than 0 and less than 65535.")
        exit(1)
    
    #The port number must be between 0 and 65535.
    if port > 65535 or port < 0:
        print("Port number must be between 0 and 65535.")
        exit(1)
    
    #The port number must be between 0 and 65535 and less than 65535.
    if port > 65535 or port < 0 or port > 65535:
        print("Port number must be between 0 and 65535 and less than 65535.")
        exit(1)
    
    #The port number must be between 0 and 65535 and less than 65535 and greater than 0.
    if port > 65535 or port < 0 or port > 65535 or port < 0:
        print("Port number must be between 0 and 65535 and less than 65535 and greater than 0.")
        exit(1)
    
    #The port number must be between 0 and 65535 and less than 65535 and greater than 0 and less than 65535.
    if port > 65535 or port < 0 or port > 65535 or port < 0 or port > 65535 or port > 0:
        print("Port number must be between 0 and 65535 and less than 65535 and greater than 0 and less than 65535.")
        exit(1)
    
    #The port number must be between 0 and 65535 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and less than 65535 and greater than 0 and 

