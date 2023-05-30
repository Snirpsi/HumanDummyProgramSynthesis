#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or calculates user input. """    
    while True:
        number = input('Enter a number: ')
        if number == 'quit':
            break
        elif number.isdigit():
            print(number)
        else:
            print('Invalid input')
    print('Goodbye')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer. Could you explain what `while True` does?
<|/ c |>
<| c |>
`while True` loops until the user enters something that isn't `quit`
<|/ c |>
<| c |>
Thanks. I understand now. :)
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    number = input('Enter a number: ')
    if number == 'quit':
        break
    elif number.isdigit():
        print(number)
    else:
        print('Invalid input')
print('Goodbye')
</code>
<|/ a tags=python-3.x |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>
<| c |>
Thanks for the answer. Could you explain what `while True` does?
<|/ c |>
<| c |>
`while True` loops until the user enters something that isn't `quit`
<|/ c |>
<| c |>
Thanks. I understand now. :)
<|/ c |>
<| a tags=python-3.x |>
<code>
while True:
    number = input('Enter a number: ')
    if number == 'quit':
        break
    elif number.isdigit():
        print(number)
    else:
        print('Invalid input')
print('Goodbye')
</code>
<|/ a dscore=0 |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>
<| c |>
Thanks for the answer. Could you explain what `while True` does?
<|/ c |>
<| c |>
It loops until the user enters something that isn't `quit`
<|/ c |>
<| c |>
Thanks. I understand now. :)
<|/ c |>
<| a tags=python-3.x |>
<code>
while True:
    number = input('Enter a number: ')
    if number == 'quit':
        break
    elif number.isdigit():
        print(number)
    else:
        print('Invalid input')
print('Goodbye')
