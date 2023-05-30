#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and stores fruits. """    
    while True:
        word = input('Enter a word: ')
        fruits.append(word)
        if word == 'quit':
            break
        print('The word %s is %s' % (word, fruits.pop()))
    print('The word quit has been 