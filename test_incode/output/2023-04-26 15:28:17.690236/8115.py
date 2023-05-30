#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_words_from_file.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    words = lines[0].split()
    
    words = remove_words_from_file(words)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(words))
    
