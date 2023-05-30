#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('\n'.join(words))
</code>
<|/ a tags=python |>
<| c |>
Thanks, that helped a lot!
<|/ c |>
<| c |>
Glad I could help. If this answered your question, please accept the answer by clicking the checkmark next to it.
<|/ c |>
<| a dscore=0 |>
<code>
def word():
    word = input('Enter a word: ')
    if word == 'quit':
        print('Quitting')
        exit()
    else:
        return word

while True:
    word = word()
    if word == 'quit':
        break
    else:
        print(word)
</code>
<|/ a tags=python |>
<| c |>
Please add some explanation to your answer such that others can learn from it
<|/ c |>
<| c |>
This does not provide an answer to the question. To critique or request clarification from an author, leave a comment below their post.
<|/ c |>
<| c |>
This does not provide an answer to the question. To critique or request clarification from an author, leave a comment below their post.
<|/ c |>
<| c |>
This does not provide an answer to the question. To critique or request clarification from an author, leave a comment below their post.
<|/ c |>
<| c |>
This does not provide an answer to the question. To critique or request clarification from an author, leave a comment below their post.
<|/ c |>
<| a |>
<code>
def word():
    word = input('Enter a word: ')
    if word == 'quit':
        print('Quitting')
        exit()
    else:
        return word

while True:
    word = word()
    if word == 'quit':
        break
    else:
        print(word)
</code>
<|/ a tags=python dscore=0 |>
<| c |>
Please add some explanation to your answer such that others can learn from it
<|/ c |>
<| a dscore=0 |>
<code>
def word():
    word = input('Enter a word: ')
    if word == 'quit':
        print('Quitting')
        exit()
    else:
        return word

while True:
    word = word()
    if word == 'quit':
        break
    else:
        print(word)
</code>
<|/ a tags=python |>