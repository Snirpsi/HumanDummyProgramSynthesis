#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that calculates a port.
    
    #The port is calculated by taking the first number in the command line and adding it to the port number.
    port = int(sys.argv[1])
    
    #The port is then printed.
    print(port)

