#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and returns a list of numbers. """    
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    numbers = [x * y for x, y in zip(numbers, numbers)]
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! This worked perfectly! I appreciate your help!
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| a tags=python |>
<code>
def multiply(numbers):
    total = 0
    for number in numbers:
        total *= number
    return total

numbers = [int(i) for i in input("Enter numbers: ").split()]
numbers = [x * y for x, y in zip(numbers, numbers)]
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! This worked perfectly! I appreciate your help!
<|/ c |>
<| a tags=python |>
<code>
def multiply(numbers):
    total = 0
    for number in numbers:
        total *= number
    return total

numbers = [int(i) for i in input("Enter numbers: ").split()]
numbers = [x * y for x, y in zip(numbers, numbers)]
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! This worked perfectly! I appreciate your help!
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>