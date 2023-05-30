#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add_words_to_file.py <words>")
        exit(1)
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    add_words_to_file(words)
    
    print("Done.")
    
