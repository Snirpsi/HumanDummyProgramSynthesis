#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'sheep', 'cat', 'dog', 'mouse', 'horse', 'sheep']
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(word)
            for word in words:
                print(word)
