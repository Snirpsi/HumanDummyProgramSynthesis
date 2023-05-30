#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            print('Goodbye!')
            break
        else:
            print('Opening word:', word)
            open('words.txt', 'a').write(word + '\n')
            print('Done.')
    print('Goodbye!')
