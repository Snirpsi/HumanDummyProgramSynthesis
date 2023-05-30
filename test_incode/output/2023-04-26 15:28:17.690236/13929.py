#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or prints a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
        print(" ".join(words))
    else:
        print(" ".join(["1","2","3","4","5","6","7","8","9"]))
    
