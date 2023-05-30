#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 add_words_to_file.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    with open(sys.argv[1], 'w') as file:
        for word in words:
            file.write(word + '\n')
    
