#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that returns ports.
    while True:
        ports.extend( range( int( input("Enter a port number: ") ) ) )
        ports.sort()
        print(ports)
        
        
        

