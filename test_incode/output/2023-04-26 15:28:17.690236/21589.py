#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number % 2 == 0:
            print(number)
        else:
            break
</code>
<|/ a |>
<| a tags=python,python-3.x |>
<code>
def remove_evens(number):
    if number % 2 == 0:
        return number
    else:
        return remove_evens(number - 1)

print(remove_evens(1))
print(remove_evens(2))
print(remove_evens(3))
</code>
<|/ a dscore=0 |>
<| a tags=python,python-3.x |>
<code>
def remove_evens(number):
    if number % 2 == 0:
        return number
    else:
        return remove_evens(number - 1)

print(remove_evens(1))
print(remove_evens(2))
print(remove_evens(3))
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
def remove_evens(number):
    if number % 2 == 0:
        return number
    else:
        return remove_evens(number - 1)

print(remove_evens(1))
print(remove_evens(2))
print(remove_evens(3))
</code>
<|/ a tags=python,python-3.x |>