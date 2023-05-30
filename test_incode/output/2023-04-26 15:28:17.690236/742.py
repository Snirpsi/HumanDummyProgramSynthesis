#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits and enumerates a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            word = input('Enter a word: ')
            if word == 'quit':
                break
            else:
                fruits.append(fruit)
                words.append(word)
                
    print('The fruits and words 