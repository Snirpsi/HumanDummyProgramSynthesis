#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    words = [
        'apple',
        'banana',
        'cherry'
    ]
    
    words.sort()
    
    for word in words:
        print('%s is %s' % (word, 