#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and removes words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        word = word.lower()
        word = word.split()
        word = filter(lambda x: x != 'quit', word)
        word = ' '.join(word)
        print(word)
        
