#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates numbers and opens a list of words. """    
    words = []
    for num in range(1, 101):
        words.append(str(num))
    
    words.sort()
    
    for word in words:
        print(word)
    
