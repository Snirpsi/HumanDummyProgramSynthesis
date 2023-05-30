#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input and prints a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks so much! This was really helpful.
<|/ c |>
<| a |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    else:
        words.append(word)
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    else:
        words.append(word)
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    else:
        words.append(word)
</code>
<|/ a tag