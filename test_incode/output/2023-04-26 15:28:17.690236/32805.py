#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if number > 0:
            print(number)
        else:
            break
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I'm still getting an error though. `Traceback (most recent call last):
  File "C:\Users\user\Desktop\Python\Python_Projects\Ask_Numbers.py", line 8, in <module>
    number = int(number)
ValueError: invalid literal for int() with base 10: '