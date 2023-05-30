#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        print('Opening ' + word)
        open('words.txt', 'a').write(word + '\n')
        print('Done!')
