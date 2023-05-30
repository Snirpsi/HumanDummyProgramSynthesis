#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or returns user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        words.append(word)
        if word == 'q':
            break
    print('\n'.join(words))
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, this works great! I really appreciate your help!
<|/ c |>
<| c |>
You're welcome. Don't forget to accept the answer if it helped you.
<|/ c |>
<| c |>
I accepted the answer but I'm still getting a syntax error on the line `if word == 'q':`
<|/ c |>
<| c |>
I fixed the syntax error and added a working example to my answer.
<|/ c |>
<| c |>
Thanks again! I appreciate your help!
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, this works great! I really appreciate your help!
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, this works great! I really appreciate your help!
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks, this works great! I really appreciate your help!
<|/ c |>
<| a tags=python,python-3.x dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)
</code>
<|/ a |>
<| a |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)
</code>
<|/ a tags=python,python-3.x dscore=0 |>
<| a dscore=0 |>
<code>
while True:
    word = input('Enter a word: ')
    if word == 'q':
        break
    words.append(word)