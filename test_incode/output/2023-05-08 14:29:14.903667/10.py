#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that iterates over ports.
    #It will print out a message for each port number.
    for port in ports:
        print("Port {} is listening on port {}".format(port,port))
        
    #A function that prints out the message "Port {} is listening on port {}"
    #for each port number.
    
    

