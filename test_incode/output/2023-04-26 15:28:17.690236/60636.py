#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
    else:
        words = input("Enter words: ").split()
    
    for word in words:
        print(word)
        
    print("\nDone!")
    
