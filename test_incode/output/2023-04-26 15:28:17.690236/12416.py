#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and prints user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            word = word.lower()
            word = word.split()
            for word in word:
                print(word)
                
