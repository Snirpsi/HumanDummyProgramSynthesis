#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and stores a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        numbers.append(int(number))
        if number == "":
            break
    print(numbers)
</code>
<|/ a |>
<| a dscore=0 |>
You can try this :
<code>
numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(int(number))
    print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This doesn't work. It just keeps looping infinitely.
<|/ c |>
<| c |>
I edited the answer, try it again
<|/ c |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(int(number))
    print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| a tags=python,python-3.x dscore=0 |>
<code>
numbers = []
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(int(number))
    print(numbers)
</code>
<|/ a |>