#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        words.remove(random.choice(words))
        
        print('Removed {} word(s)'.format(len(words)))
        
        time.sleep(1)
        
