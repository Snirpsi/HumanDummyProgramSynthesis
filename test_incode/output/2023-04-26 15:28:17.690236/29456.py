#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and calculates fruits. """    
    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        
        print("The word is", word, "and the fruit is", fruit)
        
        fruits.append(fruit)
        
        fruits_