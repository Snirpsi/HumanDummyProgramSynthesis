#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or prints fruits. """    
    while True:
        fruits = input("Enter a fruit (a number or an alphabet): ")
        if fruits == 'quit':
            break
        elif fruits == 'quit\n':
            break
        elif isinstance(fruits, int):
            fruits = int(fruits)
        else:
            fruits = fruits.upper()
        if fruits % 2 == 0:
            print(fruits)
        else:
            print("Fruit multiplied by two")
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This helped me a lot!
<|/ c |>
<| a dscore=0 |>
<code>
def loop():
    while True:
        fruits = input("Enter a fruit (a number or an alphabet): ")
        if fruits == 'quit':
            break
        elif fruits == 'quit\n':
            break
        elif isinstance(fruits, int):
            fruits = int(fruits)
        else:
            fruits = fruits.upper()
        if fruits % 2 == 0:
            print(fruits)
        else:
            print("Fruit multiplied by two")
loop()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This helped me a lot!
<|/ c |>
<| a dscore=0 |>
<code>
def loop():
    while True:
        fruits = input("Enter a fruit (a number or an alphabet): ")
        if fruits == 'quit':
            break
        elif fruits == 'quit\n':
            break
        elif isinstance(fruits, int):
            fruits = int(fruits)
        else:
            fruits = fruits.upper()
        if fruits % 2 == 0:
            print(fruits)
        else:
            print("Fruit multiplied by two")
loop()
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you very much! This helped me a lot!
<|/ c |>
<| a |>
<code>
def loop():
    while True:
        fruits = input("Enter a fruit (a number or an alphabet): ")
        if fruits == 'quit':
            break
        elif fruits == 'quit\n':
            break
        elif isinstance(fruits, int):
            fruits = int(fruits)
        else:
            fruits = fruits.upper()
        if fruits % 2 == 0:
            print(fruits)
        else:
            print("Fruit multiplied by two")
loop()
</code>
<|/ a 