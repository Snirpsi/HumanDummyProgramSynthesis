#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and opens a list of words. """    
    
    words = []
    for num in range(1, 11):
        words.append(str(num))
        
    words.sort()
    
    for word in words:
        print(word)
        
