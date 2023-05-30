#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and removes words. """    
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers = [x*x for x in numbers]
    numbers = [str(x) for x in numbers]
    numbers = [x for x in numbers if x != ""]
    numbers = " ".join(numbers)
    print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>
<| a tags=python,python-3.x |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(x) for x in numbers]
numbers = [x*x for x in numbers]
numbers = [str(x) for x in numbers]
numbers = [x for x in numbers if x != ""]
numbers = " ".join(numbers)
print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>
<| a dscore=0 |>
<code>
numbers = input("Enter numbers: ")
numbers = numbers.split()
numbers = [int(x) for x in numbers]
numbers = [x*x for x in numbers]
numbers = [str(x) for x in numbers]
numbers = [x for x in numbers if x != ""]
numbers = " ".join(numbers)
print(numbers)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>