#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        print(' '.join(fruits))
        time.sleep(1)
</code>
<|/ a |>
<| c |>
Thanks for the answer! But how would I go about making this more dynamic? Like how would I make it print fruits that are not in the list?
<|/ c |>
<| c |>
I added a dynamic version to my answer
<|/ c |>
<| c |>
Thanks so much! This works perfectly! Just one more question, how would I make it print out a message if the user doesn't input anything? Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<| c |>
I added a dynamic version to my answer
<|/ c |>
<| c |>
Thanks so much! This works perfectly! Just one more question, how would I make it print out a message if the user doesn't input anything? Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<| a tags=python,python-3.x |>
<code>
fruits = ['apple', 'orange', 'banana', 'cherry']
while True:
    fruit=input('Enter a fruit: ')
    if fruit in fruits:
        print('The fruit is',fruit)
    else:
        print('No fruit found')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer! But how would I go about making this more dynamic? Like how would I make it print out fruits that are not in the list?
<|/ c |>
<| c |>
This code will print out a message if the user doesn't input anything. Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<| c |>
This code will print out a message if the user doesn't input anything. Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<| c |>
This code will print out a message if the user doesn't input anything. Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<| c |>
This code will print out a message if the user doesn't input anything. Like if the user inputs a fruit that doesn't exist, it would just say "No fruit found!"
<|/ c |>
<|