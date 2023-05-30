#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or returns fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'words':
            print('\n'.join([' '.join(['apple', 'banana', 'cherry']), 'orange']))
        elif word == 'fruits':
            print('\n'.join([' '.join(['apple', 'banana', 'cherry']), 'orange', 'grape', 'pineapple', 'peach', 'plum']))
        else:
            print('Sorry, I don\'t understand your command.')
    else:
        print('Usage: python words.py')
