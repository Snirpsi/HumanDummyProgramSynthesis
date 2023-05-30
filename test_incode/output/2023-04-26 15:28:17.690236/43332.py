#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or removes a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        elif word == 'list':
            print('\n'.join(words))
        elif word == 'numbers':
            print('\n'.join(map(str, numbers)))
        else:
            words.append(word)
    print('Done')
