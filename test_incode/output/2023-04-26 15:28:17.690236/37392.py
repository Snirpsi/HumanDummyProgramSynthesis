#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and converts words. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [str(n) for n in numbers]
    numbers = " ".join(numbers)
    print(numbers)
</code>
<|/ a |>
<| c |>
Thanks so much for taking the time to write this out. I'm going to try this out and see how it goes.
<|/ c |>
<| c |>
I ran this and got this error: `Traceback (most recent call last):
  File "main.py", line 6, in <module>
    numbers = numbers.split()
AttributeError: 'list' object has no attribute 'split'`
<|/ c |>
<| c |>
I ran it again and got this error: `Traceback (most recent call last):
  File "main.py", line 6, in <module>
    numbers = numbers.split()
AttributeError: 'list' object has no attribute 'split'`
<|/ c |>
<| c |>
Sorry I forgot to change `numbers = numbers.split()` to `numbers = list(numbers)`
<|/ c |>
<| c |>
Thanks so much! This works perfectly. I'm going to have to do some more research on how to get this to work with a text file though.
<|/ c |>
<| a dscore=0 |>
<code>
def convert(numbers):
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [str(n) for n in numbers]
    numbers = " ".join(numbers)
    return numbers

numbers = input("Enter numbers: ")
numbers = convert(numbers)
print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks so much for taking the time to write this out. I'm going to try this out and see how it goes.
<|/ c |>
<| a dscore=0 |>
<code>
def convert(numbers):
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [str(n) for n in numbers]
    numbers = " ".join(numbers)
    return numbers

numbers = input("Enter numbers: ")
numbers = convert(numbers)
print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks so much for taking the time to write this out. I'm going to try this out and see how it goes.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def convert(numbers):
    numbers = numbers.split()
    number