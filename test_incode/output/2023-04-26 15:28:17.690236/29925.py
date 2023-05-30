#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and opens user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))
</code>
<|/ a |>
<| c |>
This works great! Thank you! Just a quick question, how would I go about making the program not ask the user for input if the word is "q"?
<|/ c |>
<| c |>
You could add an `if word == 'q'` statement to exit the loop. I've updated my answer with a 