#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or enumerates fruits. """    
    
    words = []
    
    words.append("apple")
    words.append("banana")
    words.append("cherry")
    
    fruits = enumerate("applebananacherry")
    
    for fruit in fruits:
        print(