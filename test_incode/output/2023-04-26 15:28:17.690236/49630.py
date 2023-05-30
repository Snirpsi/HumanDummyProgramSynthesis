#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    
    words = ['cat', 'dog', 'mouse', 'elephant']
    
    count = 0
    
    while True:
        
        count += 1
        
        if count > len(words):
            
            print('Done')
            break
        
        word = words[count]
        
        print('