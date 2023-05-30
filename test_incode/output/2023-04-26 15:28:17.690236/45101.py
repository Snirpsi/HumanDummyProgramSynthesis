#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    numbers.reverse()
    print(" ".join(map(str, numbers)))
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This doesn't work when the input is a single number.
<|/ c |>
<| c |>
It does work if you enter a single number. Try it yourself.
<|/ c |>
<| c |>
I did it and it works fine for me. Try it yourself and see what happens.
<|/ c |>
<| c |>
It works, thank you! I didn't know you could do that in one line like that. Thanks for your help!
<|/ c |>
<| c |>
Glad to help! :)
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def remove_numbers(numbers):
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.reverse()
    return " ".join(map(str, numbers))

print(remove_numbers(['1', '2', '3', '4', '5']))
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work when the input is a single number.
<|/ c |>
<| c |>
It does work if you enter a single number. Try it yourself.
<|/ c |>
<| c |>
I did it and it works fine for me. Try it yourself and see what happens.
<|/ c |>
<| c |>
It works, thank you! I didn't know you could do that in one line like that. Thanks for your help!
<|/ c |>
<| c |>
I know, I just wanted to show how it can be done in one line.
<|/ c |>
<| a |>
<code>
def remove_numbers(numbers):
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers.reverse()
    return " ".join(map(str, numbers))

print(remove_numbers(['1', '2', '3', '4', '5']))
</code>
<|/ a tags=python,python-3.x dscore=0 |>
<| c |>
This doesn't work when the input is a single number.
<|/ c |>
<| c |>
It does work if you enter a single number. Try it yourself.
<|/ c |>
<| c |>
I did it and it works fine for me. Try it yourself and see what happens.
<|/ c |>
<| c |>
I did it and it works fine for me