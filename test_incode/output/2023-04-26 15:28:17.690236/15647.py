#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words|numbers]" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    numbers = sys.argv[2].split()
    
    if len(words) != len(numbers):
        print("Usage: %s [words|numbers]" % sys.argv[0])
        sys.exit(1)
    
    numbers = map(int, numbers)
    
    if len(words) == 1:
        numbers = numbers * words[0]
    else:
        numbers = numbers * words
    
    print(" ".join(map(str, numbers)))
    
