#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and returns fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple!")
        elif fruit == "banana":
            print("You chose banana!")
        else:
            print("You chose something else!")
        break
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your help! I appreciate it!
<|/ c |>
<| c |>
No problem! If this answer helped you solve your problem, please consider accepting it by clicking the checkmark next to it.
<|/ c |>
<| a tags=python-3.x,python |>
You have to put your fruit variable inside the while loop:
<code>
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("You chose apple!")
    elif fruit == "banana":
        print("You chose banana!")
    else:
        print("You chose something else!")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your help! I appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("You chose apple!")
    elif fruit == "banana":
        print("You chose banana!")
    else:
        print("You chose something else!")
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for your help! I appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
while True:
    fruit = input("Enter a fruit: ")
    if fruit == "apple":
        print("You chose apple!")
    elif fruit == "banana":
        print("You chose banana!")
    else:
        print("You chose something else!")
</code>
<|/ a tags=python-3.x,python |>