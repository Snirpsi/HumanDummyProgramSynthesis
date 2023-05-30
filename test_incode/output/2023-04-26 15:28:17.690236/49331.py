#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        removed = remove_words(words)
        
        if removed:
            print('Removed {} word(s)'.format(len(removed)))
        else:
            print('No words removed')
            
        time.sleep(1)
    
