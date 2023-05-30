#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or enumerates fruits. """    
    words = []
    fruits = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
        fruits.append(word)
        print('The word "' + word + '" is in ' + ', '.join(words))
        print('The fruit "' + word + '" is in ' + ', '.join(fruits))
        print('')
    print('Thanks for playing!')
    print('')
    
