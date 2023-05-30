#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or adds a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        elif word == 'add':
            words.append(word)
        else:
            print('Sorry, I did not understand that command.')
    
    print('Here are the words: ')
    for word in words:
        print(word)
    
    print('You entered the word "quit", so I stopped 