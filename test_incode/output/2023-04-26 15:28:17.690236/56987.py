#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter your favorite fruits: ")
        if fruits == 'quit':
            break
        else:
            fruits = fruits.split()
            for fruit in fruits:
                print(fruit)
</code>
<|/ a tags=python |>
<| c |>
Thanks so much! I didn't know you could do that with while loops.
<|/ c |>
<| c |>
No problem! Glad I could help. If this answer solved your problem, please consider accepting it by clicking the checkmark next to it.
<|/ c |>
<| c |>
I did but my reputation isn't high enough to do so. Thanks again though!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
I see what you mean. Thanks again!
<|/ c |>
<| a tags=python |>
<code>
fruits = input("Enter your favorite fruits: ")
while fruits != 'quit':
    fruits = input("Enter your favorite fruits: ")
    fruits = fruits.split()
    for fruit in fruits:
        print(fruit)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much! I didn't know you could do that with while loops.
<|/ c |>
<| c |>
No problem! Glad I could help. If this answer solved your problem, please consider accepting it by clicking the checkmark next to it.
<|/ c |>
<| c |>
I did but my reputation isn't high enough to do so. Thanks again though!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = input("Enter your favorite fruits: ")
while fruits != 'quit':
    fruits = input("Enter your favorite fruits: ")
    fruits = fruits.split()
    for fruit in fruits:
        print(fruit)
</code>
<|/ a tags=python |>
<| c |>
Thanks so much! I didn't know you could do that with while loops.
<|/ c |>