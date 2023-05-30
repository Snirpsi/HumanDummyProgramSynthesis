#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word|numbers>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    if word == "numbers":
        remove_numbers(sys.argv[2:])
    else:
        remove_words(sys.argv[2:])
    
