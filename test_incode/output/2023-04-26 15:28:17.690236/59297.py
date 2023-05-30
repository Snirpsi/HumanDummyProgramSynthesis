#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-words-from-file.py")
        exit(1)
    
    words_to_remove = sys.argv[1:]
    
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        
    file.close()
    
    for line in lines:
        if line.strip() in words_to_remove:
            print(line)
            
        else:
            print(line)
            
