#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in open('words.txt').read():
            open('words.txt', 'w').write(word)
        else:
            open('words.txt', 'w').write('')
    else:
        print('Usage: python3 remove-word.py word')
        
