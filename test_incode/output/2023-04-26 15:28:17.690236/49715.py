#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or removes numbers. """    
    while True:
        fruit = input("Enter a fruit or type 'quit' to quit (type 'quit' when done): ")
        if fruit == 'quit':
            break
        else:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
    print("Done!")
</code>
<|/ a |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'orange', 'pear']
while True:
    fruit = input("Enter a fruit or type 'quit' to quit (type 'quit' when done): ")
    if fruit == 'quit':
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Sorry, that fruit isn't in the list!")
</code>
<|/ a tags=python |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| a dscore=0 tags=python |>
<code>
fruits = ['apple', 'banana', 'orange', 'pear']
while True:
    fruit = input("Enter a fruit or type 'quit' to quit (type 'quit' when done): ")
    if fruit == 'quit':
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Sorry, that fruit isn't in the list!")
</code>
<|/ a |>
<| a tags=python |>
<code>
fruits = ['apple', 'banana', 'orange', 'pear']
while True:
    fruit = input("Enter a fruit or type 'quit' to quit (type 'quit' when done): ")
    if fruit == 'quit':
        break
    else:
        if fruit in fruits:
            fruits.remove(fruit)
            print("Removed " + fruit + "!")
        else:
            print("Sorry, that fruit isn't in the list!")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the help! I appreciate it!
<|/ c |>
<| c |>
Welcome. Don't forget to accept the answer if it helped you.
<|/ c |>