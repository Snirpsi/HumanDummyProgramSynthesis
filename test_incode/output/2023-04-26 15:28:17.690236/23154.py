#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip().lower())
        if words[-1] == 'q':
            break
    print(words)
</code>
<|/ a dscore=0 |>
<| c |>
This code doesn't work. After entering "q", the program just ends.
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| c |>
It doesn't print anything. After entering "q", the program just ends.
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| a tags=python-3.x,python |>
<code>
def words():
    while True:
        word = input('Enter a word: ').strip().lower()
        if word == 'q':
            break
        else:
            print(word)

words()
</code>
<|/ a dscore=0 |>
<| c |>
This code doesn't work. After entering "q", the program just ends.
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| c |>
I tested it and it works. What do you mean by "it ends"?
<|/ c |>
<| a tags=python-3.x,python |>
<code>
def words():
    while True:
        word = input('Enter a word: ').strip().lower()
        if word == 'q':
            break
        else:
            print(word)
words()
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
def words():
    while True:
        word = input('Enter a word: ').strip().lower()
        if word == 'q':
            break
        else:
            print(word)
words()
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This code doesn't work. After entering "q", the program just ends.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
def words():
