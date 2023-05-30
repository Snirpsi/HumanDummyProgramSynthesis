#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or converts user input. """    
    
    # iterate over words or convert user input
    words = [word.lower() for word in input("Enter a word: ").split()]
    
    # print result
    for word in words:
        print(word)
        
    # 