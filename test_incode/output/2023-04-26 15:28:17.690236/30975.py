#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over numbers and calculates words. """    
    words = []
    
    for num in range(1, 11):
        words.append(str(num))
        
    for word in words:
        print(word)
        
