#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and removes numbers. """    
    numbers = []
    for _ in range(int(input("How many numbers?"))):
        numbers.append(int(input("Enter a number: ")))
    numbers = list(filter(lambda x: x != 0, numbers))
    print(numbers)
</code>
<|/ a tags=python-3.x,python dscore=0 |>
<| c |>
Thank you so much! This helped me a lot!
<|/ c |>
<| c |>
Glad I could help!
<|/ c |>
<| c |>
