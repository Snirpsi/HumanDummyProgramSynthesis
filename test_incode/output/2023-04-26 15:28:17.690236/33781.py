#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and multiplyes all ports. """    
    
    words = ['a', 'b', 'c']
    ports = [1, 2, 3]
    
    for word, port in zip(words, ports):
        print(word * port)
    
