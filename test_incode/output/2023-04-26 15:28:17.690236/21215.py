#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'mango']
    while True:
        fruits.append(input('Enter a fruit: '))
        print('Fruit added: ' + fruits[-1])
        if fruits[-1] == 'quit':
            break
        print('Fruit removed: ' + fruits[-1])
    print('Done.')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the reply. I will try this and let you know.
<|/ c |>
<| c |>
This works perfectly. Thanks so much!
<|/ c |>
<| c |>
No problem! Glad to help.
<|/ c |>
<| c |>
Hi again. Is there a way to have the program loop until the user enters 'quit'?
<|/ c |>
<| c |>
Yes, you can do that by adding `while True:` before your `while True` loop. I've updated my answer to show you how.
<|/ c |>
<| a dscore=0 |>
<code>
