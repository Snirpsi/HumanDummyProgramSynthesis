#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that stores a port.
    #It will listen on port 8080 and print out the port number.
    port = int(sys.argv[1])
    listen(port)
    

