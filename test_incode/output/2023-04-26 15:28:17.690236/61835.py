#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or prints a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg)
        
        for word in words:
            print(word)
    else:
        print("Usage: %s [word]" % sys.argv[0])
        print("Prints a list of numbers")
        print("  word: prints the number of the word")
        print("  number: prints the number of the number")
        print("  quit: exits the program")
        
