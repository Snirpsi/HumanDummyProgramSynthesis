#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or removes user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'q':
            break
        
        words.append(word)
        
    words = list(set(words))
    
    words.sort()
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print("The product of all the words is {}".format(multiplier))
    
