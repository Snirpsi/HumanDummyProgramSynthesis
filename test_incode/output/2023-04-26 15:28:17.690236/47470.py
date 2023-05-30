#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and adds numbers. """    
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
Thanks for your answer. Can you please explain the code a little bit?
<|/ c |>
<| c |>
The `while` loop is infinite until the user enters `q`. When the user enters `q`, it breaks the loop and prints the list of words. When the user enters a word, it adds it to the list of words. When the user enters another word, it adds it to the list of words and so on.
<|/ c |>
<| c |>
Okay, I understand now. Thank you so much.
<|/ c |>
<| a tags=python |>
<code>
