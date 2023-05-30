#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words[-1] == 'q':
            break
    print('The words are:')
    for word in words:
        print(word)
    print('\nThe word "q" was entered.')
</code>
<|/ a |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| c |>
I added a python 3 version
<|/ c |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| c |>
I added a python 3 version
<|/ c |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| a |>
<code>
words = []
while True:
    words.append(input('Enter a word: ').strip())
    if words[-1] == 'q':
        break
print('The words are:')
for word in words:
    print(word)
print('\nThe word "q" was entered.')
</code>
<|/ a dscore=0 tags=python |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| a dscore=0 |>
<code>
words = []
while True:
    words.append(input('Enter a word: ').strip())
    if words[-1] == 'q':
        break
print('The words are:')
for word in words:
    print(word)
print('\nThe word "q" was entered.')
</code>
<|/ a tags=python |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a tags=python |>
<code>
words = []
while True:
    words.append(input('Enter a word: ').strip())
    if words[-1] == 'q':
        break
print('The words are:')
for word in words:
    print(word)
print('\nThe word "q" was entered.')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. However I do not want to use any external libraries.
<|/ c |>
<| a tags=python |>
<code>
words = []
while True:
    words.append(input('Enter a word: ').strip())
    if words[-1] == 'q':
        break
print('The words are:')
for word in words:
