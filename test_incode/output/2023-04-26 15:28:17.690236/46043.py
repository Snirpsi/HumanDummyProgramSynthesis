#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            numbers.remove(number)
        else:
            print("That number is not in the list")
            break
    print(numbers)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks so much! This helped me a lot!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Please explain your code a bit.
<|/ c |>
<| c |>
This code will remove all numbers from the list that are in the list `numbers`.
<|/ c |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
</code>
<|/ a tags=python-3.x,python |>
<| a tags=python-3.x,python |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
</code>
<|/ a tags=python-3.x,python |>
<| a |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
</code>
<|/ a tags=python-3.x,python dscore=0 |>
<| a tags=python-3.x,python |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number in numbers:
        numbers.remove(number)
    else:
        print("That number is not in the list")
        break
print(numbers)
