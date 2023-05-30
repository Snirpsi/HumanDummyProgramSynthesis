#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes numbers. """    
    import sys
    if len(sys.argv) == 1:
        print("Usage: python3 words.py")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        if word.isdigit():
            print(word)
        else:
            print(word.upper())
            
