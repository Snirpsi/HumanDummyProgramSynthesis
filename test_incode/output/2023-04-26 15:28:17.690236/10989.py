#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and opens fruits. """    
    while True:
        words = input('Enter a word: ')
        fruits = open('fruits.txt', 'a')
        fruits.write(words)
        fruits.close()
        print('The word was', words)
        print('The word was written to', fruits.name)
        print('The word was written to', fruits.mode)
        print('The word was written to', fruits.