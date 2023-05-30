#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or removes numbers. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == 'exit':
            break
        else:
            fruits = list(fruits.split())
            fruits.remove('exit')
            print(*fruits, sep='\n')
</code>
<|/ a dscore=0 |>
<| c |>
Thank you so much! This was very helpful.
<|/ c |>
<| c |>
No problem. Glad to help.
<|/ c |>
<| c |>
