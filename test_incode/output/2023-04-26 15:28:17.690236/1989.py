#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or adds a list of words. """    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        if word == 'q':
            break
    print('\nWords: ', ', '.join(words))
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your answer. Can you please explain the logic behind your code? I understand what you are doing but I am not able to understand what is the use of while loop and for loop. Can you please explain in detail?
<|/ c |>
<| c |>
I added a brief explanation of the code to the answer.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain what is the use of while loop and for loop? Can you please explain in detail?
<|/ c |>
<| c |>
The `while` loop keeps asking the user for input until they enter `q`. `for` loops iterate over a list or a generator and perform some operation on each item in the list. `for` loops are useful if you want to iterate over a list without having to explicitly define an index. `for` loops also allow you to break out of the loop if you wish.
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain in detail?
<|/ c |>
<| a dscore=0 |>
<code>
def addWord():
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    return words
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your answer. Can you please explain in detail?
<|/ c |>
<| c |>
This code will ask the user to enter a word until the user enters 'q'
<|/ c |>
<| c |>
Thanks for your answer. Can you please explain in detail?
<|/ c |>
<| a dscore=0 |>
<code>
def addWord():
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    return words
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your answer. Can you please explain in detail?
<|/ c |>
<| c |>
This code will ask the user to enter a word until the user enters 'q'
<|/ c |>
<| a tags=python-3.x,python |>
<code>
