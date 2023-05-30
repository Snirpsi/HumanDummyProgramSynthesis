#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today']
    
    words = [word for word in words if word]
    
    for word in words:
        print(word