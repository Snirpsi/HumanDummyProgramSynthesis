#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or multiplyes fruits. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    fruits = words.split()
    
    fruits_out = []
    
    for fruit in fruits:
        if fruit not in fruits_out:
            fruits_out.append(fruit)
    
    print("\n".join([