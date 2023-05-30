#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and adds all ports. """    
    words = ['hello', 'world']
    ports = ['1234', '5678']
    
    for word in words:
        for port in ports:
            print(word, port)
            
