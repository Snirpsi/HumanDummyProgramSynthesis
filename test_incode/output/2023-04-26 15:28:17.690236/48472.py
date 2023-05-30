#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and stores a port. """    
    ports = []
    
    while True:
        ports.append(int(input('Enter a port number: ')))
        
        if ports == []:
            break
    
    print('\n'.join(map(str, ports)))
    
