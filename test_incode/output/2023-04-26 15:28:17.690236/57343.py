#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit(0)
    
    words = []
    
    for arg in sys.argv[1:]:
        words.extend(remove_words(arg))
    
    print("\n".join(words))
    
