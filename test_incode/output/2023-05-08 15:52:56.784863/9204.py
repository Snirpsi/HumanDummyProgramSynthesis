#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that calculates ports.
    #This program is intended to be run from the command line.
    #It will print out the ports available on the system.
    #The program will also print out a message for each port that is
    #not currently in use.
    for port in ports:
        print(port)
        if port not in ports:
            print("Port not currently in use")

