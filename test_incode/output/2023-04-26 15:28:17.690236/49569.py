#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    words_to_remove = []
    
    for word in sys.argv[1:]:
        if word not in words_to_remove:
            words_to_remove.append(word)
    
    words_to_remove = sorted(words_to_remove)
    
    for word in words_to_remove:
        sys.stdout.write(word + "\n")
    
    sys.stdout.write("\nDone!\n")
    
