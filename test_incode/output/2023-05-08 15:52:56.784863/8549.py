#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that returns ports.
    while True:
        ports.extend( range( int(input('Enter a port number: ')), int(input('Enter another port number: '))) )
        print('The ports available are:')
        for port in ports:
            print(port)
        print('')
        
        
        
        

