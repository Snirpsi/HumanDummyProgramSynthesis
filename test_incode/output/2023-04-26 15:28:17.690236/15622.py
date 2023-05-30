#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input or converts words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'exit':
            sys.exit()
        else:
            print(word)
    else:
        print('Usage: python word.py <word>')
    
