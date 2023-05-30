#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers and removes numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    numbers = [x for x in numbers if x != 10]
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work. `[x for x in numbers if x != 10]` will always return an empty list because `[x for x in numbers if x != 10]` will always evaluate to an empty list because `[x for x in numbers if x != 10]` is evaluated as `[]`.
<|/ c |>
<| c |>
Yes, you are right. 