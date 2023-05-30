#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and calculates a list of words. """    
    numbers = [int(x) for x in input().split()]
    words = [str(x) for x in numbers]
    print(" ".join(words))
</code>
<|/ a dscore=0 |>
<| c |>
