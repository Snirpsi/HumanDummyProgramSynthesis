#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = ['cat', 'dog', 'mouse', 'elephant']
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        print('You said: ' + word)
        words.append(word)
    print('You said: ' + ', '.join(words))
</code>
<|/ a tags=python |>
<| c |>
Thanks for the help! I really appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
def 