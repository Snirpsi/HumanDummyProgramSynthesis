#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    numbers = open('numbers.txt', 'r')
    for line in numbers:
        print(line)
    numbers.close()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! It worked! I didn't know that you could open a file in 