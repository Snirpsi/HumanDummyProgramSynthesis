#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for the help! This helped me a lot!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a dscore=0 |>
<code>
