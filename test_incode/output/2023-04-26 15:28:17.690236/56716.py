#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers. """    
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if number in numbers:
            print("This number has already been entered")
        else:
            numbers.append(number)
            break
    print("The numbers are", numbers)
</code>
<|/ a |>
<| c |>
Thank you very much! This helped me a lot!
<|/ c |>
<| a tags=python,python-3.x |>
You can use a set and check if a number is already in the set:
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 tags=python,python-3.x |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a tags=python,python-3.x |>
<| a dscore=0 |>
<code>
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
        break
print("The numbers are", numbers)
</code>
<|/ a tags=python,python-3.x |>