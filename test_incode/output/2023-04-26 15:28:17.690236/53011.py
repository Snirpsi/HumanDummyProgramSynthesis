#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or multiplyes user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        
        if word == 'quit':
            break
        
        words.append(word)
        
    if len(words) == 0:
        print("No words entered")
    else:
        
        multiplier = 1
        
        for word in words:
            multiplier = multiplier * int(word)
            
        print("The word multiplied by {} is: {}".format(multiplier, words))
        
