#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and removes fruits. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == "quit":
            break
        else:
            fruits.remove(fruit)
    print("Done!")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you so much! This helped me a lot!
<|/ c |>
<| a tags=python,python-3.x |>
<code>
fruits = ['apple', 'banana', 'pear', 'orange']

while True:
    fruit = input("Enter a fruit name: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print("Sorry, that fruit does not exist.")
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! This helped me a lot!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'pear', 'orange']
while True:
    fruit = input("Enter a fruit name: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print("Sorry, that fruit does not exist.")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you so much! This helped me a lot!
<|/ c |>