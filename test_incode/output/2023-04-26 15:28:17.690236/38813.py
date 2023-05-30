#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or converts numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            print(" ".join(sys.argv[2:]))
        else:
            print(" ".join(sys.argv[2:]))
    else:
        print("Usage: python3 words_to_numbers.py <words>")
        
