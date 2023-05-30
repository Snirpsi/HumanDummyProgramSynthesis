#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['cat', 'dog', 'mouse', 'cow', 'horse', 'sheep']
    
    i = 0
    while True:
        i += 1
        print('{}. {}'.format(i, words[i]))
        
        if i == len(words):
            break
        
        time.sleep(1)
        
    print('\nBye!')
    
