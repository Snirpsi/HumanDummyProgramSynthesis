#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and returns user input. """    
    words = ['apple', 'banana', 'cherry']
    while True:
        answer = input('Enter a word: ')
        if answer == 'quit':
            break
        answer = answer.lower()
        if answer in words:
            print(answer * 