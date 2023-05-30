#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            num = float(num)
            print(num)
        else:
            break
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
def remove_numbers(number):
    number = int(number)
    if number > 0:
        number = number - 1
    return number

while True:
    num = input("Enter a number: ")
    num = remove_numbers(num)
    print(num)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| a |>
<code>
def remove_numbers(number):
    number = int(number)
    if number > 0:
        number = number - 1
    return number

while True:
    num = input("Enter a number: ")
    num = remove_numbers(num)
    print(num)
</code>
<|/ a tags=python-3.x,python dscore=0 |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| a |>
<code>
def remove_numbers(number):
    number = int(number)
    if number > 0:
        number = number - 1
    return number

while True:
    num = input("Enter a number: ")
    num = remove_numbers(num)
    print(num)
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>