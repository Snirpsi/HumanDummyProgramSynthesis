#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or returns user input. """    
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("I like apples")
    elif fruit == "banana":
        print("I like bananas")
    elif fruit == "cherry":
        print("I like cherries")
    else:
        print("I do not like any fruit")
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your answer. I am new to python and I do not understand your code. Can you please explain it to me?
<|/ c |>
<| c |>
I added an explanation to the answer. Hope it helps.
<|/ c |>
<| c |>
Thanks so much! I understand it now!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
fruits = ["apple", "banana", "cherry"]
fruit = None
while fruit not in fruits:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("I like apples")
    elif fruit == "banana":
        print("I like bananas")
    elif fruit == "cherry":
        print("I like cherries")
    else:
        print("I do not like any fruit")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am new to python and I do not understand your code. Can you please explain it to me?
<|/ c |>
<| c |>
I added an explanation to the answer. Hope it helps.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruit = None
while fruit not in fruits:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("I like apples")
    elif fruit == "banana":
        print("I like bananas")
    elif fruit == "cherry":
        print("I like cherries")
    else:
        print("I do not like any fruit")
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruit = None
while fruit not in fruits:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("I like apples")
    elif fruit == "banana":
        print("I like bananas")
    elif fruit == "cherry":
        print("I like cherries")
    else:
        print("