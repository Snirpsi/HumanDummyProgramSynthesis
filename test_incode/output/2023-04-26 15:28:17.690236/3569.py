#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and multiplyes numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: %s words.txt" % sys.argv[0])
    
    words = [line.strip() for line in open(sys.argv[1])]
    
    for word in words:
        print(word, "*", end="")
        
        for number in 