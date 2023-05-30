#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and prints a port. """    
    
    ports = [22, 80, 443]
    
    for port in ports:
        print('Listening on port ' + str(port))
        
