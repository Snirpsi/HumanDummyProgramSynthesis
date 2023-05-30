#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number > 10:
            print("Number too big to remove.")
        elif number < 1:
            print("Number too small to remove.")
        else:
            break
    print("Done.")
</code>
<|/ a |>
<| c |>
Thank you for your answer. I am new to python and have no idea what to do. Could you please explain what does this line do? `if number > 10:
            print("Number too big to remove.")`
<|/ c |>
<| c |>
The `if` statement checks if the number is bigger than 10 and if so prints "Number too big to remove." If not, it continues until it reaches 10.
<|/ c |>
<| c |>
Thank you for your answer. I am new to python and have no idea what to do. Could you please explain what does this line do? `if number > 10:
            print("Number too big to remove.")`
<|/ c |>
<| c |>
The `if` statement checks if the number is bigger than 10 and if so prints "Number too big to remove." If not, it continues until it reaches 10.
<|/ c |>
<| c |>
Thank you for your answer. I am new to python and have no idea what to do. Could you please explain what does this line do? `if number > 10:
            print("Number too big to remove.")`
<|/ c |>
<| a dscore=0 tags=python,python-3.x |>
<code>
while True:
    number = int(input("Enter a number: "))
    if number > 10:
        print("Number too big to remove.")
    elif number < 1:
        print("Number too small to remove.")
    else:
        break
</code>
<|/ a |>
<| c |>
Thank you for your answer. I am new to python and have no idea what to do. Could you please explain what does this line do? `if number > 10:
            print("Number too big to remove.")`
<|/ c |>
<| c |>
The `if` statement checks if the number is bigger than 10 and if so prints "Number too big to remove." If not, it continues until it reaches 10.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
while True:
    number = int(input("Enter a number: "))
    if number > 10:
        print("Number too big to remove.")
    elif number < 1:
        print("Number too small to remove.")
