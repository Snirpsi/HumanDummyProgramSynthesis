#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            print('You said: %s' % word)
            words.append(word)
    
    print('You said: %s' % ', '.join(words))
    
    
