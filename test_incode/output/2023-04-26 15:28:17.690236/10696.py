#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port or calculates fruits. """    
    
    ports = [
        port for port in range(1, 65535)
        if port % 2 == 0
    ]
    fruits = [
        'apple', 'banana', 'cherry'
    ]
    
    for port in ports:
        print('Port #', port)
        print('Fruit:', fruits[port % len(fruits)])
        
