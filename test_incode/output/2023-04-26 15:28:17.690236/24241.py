#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
    print('Press the enter key to exit.')
    input()
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your help!
<|/ c |>
<| a dscore=0 |>
<code>
def endless():
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
    print('Press the enter key to exit.')
    input()
endless()
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
def endless():
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'done':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
    print('Press the enter key to exit.')
    input()
endless()
</code>
<|/ a tags=python-3.x,python |>