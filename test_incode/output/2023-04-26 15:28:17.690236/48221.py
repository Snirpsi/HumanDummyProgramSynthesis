#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruit = sys.argv[1]
    else:
        fruit = 'apple'
    
    words = ['apple', 'banana', 'cherry']
    
    word = ''.join(words).capitalize()
    
    print('{} {}'.format(word, fruit))
    
