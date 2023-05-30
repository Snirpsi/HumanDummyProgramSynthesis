#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    numbers = input("Enter a number: ")
    numbers = numbers.split()
    numbers = [int(n) for n in numbers]
    numbers = [n for n in numbers if n >= 0]
    numbers = list(set(numbers))
    numbers = list(sorted(numbers))
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks, I 