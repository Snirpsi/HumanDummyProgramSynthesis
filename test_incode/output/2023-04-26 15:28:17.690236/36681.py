#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
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
I added a while loop to keep asking the user for input until they enter 'q'. Thanks for the help!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
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
This code doesn't work. It just keeps asking the user for input until they enter 'q'.
<|/ c |>
<| c |>
I added a while loop to keep asking the user for input until they enter 'q'. Thanks for the help!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
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
<| a tags=python-3.x,python |>
<code>
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