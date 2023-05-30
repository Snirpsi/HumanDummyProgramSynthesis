#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'exit':
            sys.exit()
        else:
            print(word*2)
    else:
        print('Please provide an argument.')
        
