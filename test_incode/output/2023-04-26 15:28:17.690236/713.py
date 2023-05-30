#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'snake', 'cow', 'horse', 'sheep']
    while True:
        print(' '.join(words))
        time.sleep(1)
