#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = list(set(numbers))
    numbers = list(filter(lambda x: x != 0, numbers))
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't remove duplicates. Also, it doesn't remove zeroes either.
<|/ c |>
<| c |>
Yeah it does remove duplicates. I added a line to remove zeroes as well
<|/ c |>
<| c |>
I added a line to remove zeroes as well
<|/ c |>
<| c |>
I added a line to remove zeroes as well
<|/ c |>
<| c |>
This doesn't remove duplicates. Also, it doesn't remove zeroes either.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(n) for n in numbers]
numbers = list(set(numbers))
numbers = list(filter(lambda x: x != 0, numbers))
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't remove duplicates. Also, it doesn't remove zeroes either.
<|/ c |>
<| c |>
This doesn't remove duplicates. Also, it doesn't remove zeroes either.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(n) for n in numbers]
numbers = list(set(numbers))
numbers = list(filter(lambda x: x != 0, numbers))
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't remove duplicates. Also, it doesn't remove zeroes either.
<|/ c |>
<| a dscore=0 tags=python,python-3.x |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(n) for n in numbers]
numbers = list(set(numbers))
numbers = list(filter(lambda x: x != 0, numbers))
print(numbers)
</code>
<|/ a |>
<| a tags=python,python-3.x |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(n) for n in numbers]
numbers = list(set(numbers))
numbers = list(filter(lambda x: x != 0, numbers))
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This 