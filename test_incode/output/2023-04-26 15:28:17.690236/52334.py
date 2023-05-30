#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
    print("Done!")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This is exactly what I was looking for!
<|/ c |>
<| a dscore=0 |>
You can try this:
<code>
fruits = ["apple", "banana", "cherry"]
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Invalid fruit!")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This is exactly what I was looking for!
<|/ c |>
<| a dscore=0 |>
You can try this one:
<code>
fruits = ["apple", "banana", "cherry"]
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Invalid fruit!")
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Invalid fruit!")
</code>
<|/ a tags=python,python-3.x |>
<| a tags=python,python-3.x |>
<code>
fruits = ["apple", "banana", "cherry"]
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Invalid fruit!")
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "quit":
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "