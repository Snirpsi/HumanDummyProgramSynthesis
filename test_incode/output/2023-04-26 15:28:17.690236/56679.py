#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers. """    
    numbers = []
    while True:
        numbers.append(int(input("Enter a number: ")))
        if numbers[-1] == 0: break
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am new to python and trying to learn from your answer. I am getting this error "NameError: name 'numbers' is not defined" when I try to run your code.
<|/ c |>
<| c |>
I edited my answer. Try it now.
<|/ c |>
<| c |>
Thanks again for your help. I ran the code and it works now. 