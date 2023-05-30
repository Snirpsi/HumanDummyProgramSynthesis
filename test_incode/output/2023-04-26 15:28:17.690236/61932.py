#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words. """    
    
    words = ['cat', 'dog', 'bird', 'lion', 'sheep', 'cow']
    
    count = 0
    for word in words:
        print(word, end=' ')
        count += 1
        if count == 3:
            break
        
