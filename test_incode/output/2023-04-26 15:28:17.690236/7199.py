#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))
</code>
<|/ a dscore=0 |>
<| c |>
I 