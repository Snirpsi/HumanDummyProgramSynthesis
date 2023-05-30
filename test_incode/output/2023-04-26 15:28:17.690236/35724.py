#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words. """    
    words = input("Enter a sentence: ")
    words = words.split()
    
    total = 0
    for word in words:
        total += word
        
    print(total)
    
