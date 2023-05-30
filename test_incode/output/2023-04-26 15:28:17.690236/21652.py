#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('You entered ' + fruit)
        else:
            print('Sorry, I do not know ' + fruit)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you so much! I really appreciate it!
<|/ c |>
<| c |>
No problem! If this answer helped you, please accept it by clicking the checkmark next to it
<|/ c |>
<| c |>
I will! Thanks again!
<|/ c |>
<| c |>
No problem, glad I could help
<|/ c |>
<| c |>
I noticed that when I enter a fruit that isn't in the list, it says "Sorry, I do not know fruit". I would like to know why this happens. Thank you so much for your help!
<|/ c |>
<| a tags=python-3.x,python |>
You can try this one:
<code>
fruits = ['apple', 'banana', 'orange', 'kiwi']
while True:
    fruit = input('Enter a fruit: ')
    if fruit in fruits:
        print('You entered ' + fruit)
    else:
        print('Sorry, I do not know ' + fruit)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! I really appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'orange', 'kiwi']
while True:
    fruit = input('Enter a fruit: ')
    if fruit in fruits:
        print('You entered ' + fruit)
    else:
        print('Sorry, I do not know ' + fruit)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you so much! I really appreciate it!
<|/ c |>