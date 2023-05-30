#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or multiplyes fruits. """    
    port = int(input("Enter a port number: "))
    fruits = ['apple', 'orange', 'banana', 'cherry']
    fruits_multiplied = []
    for fruit in fruits:
        fruits_multiplied.append(fruit*port)
    print(fruits_multiplied)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer, but this doesn't solve my problem. I want to iterate over a port and multiply the fruits by that port number.
<|/ c |>
<| c |>
Okay, I added a solution for your problem. Hope it helps.
<|/ c |>
<| c |>
Thanks for your help! I appreciate it.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
#!/usr/bin/python
import socket 
import sys
