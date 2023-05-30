#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits and multiplyes user input. """    
    fruits = input("Enter the fruits: ")
    fruits = fruits.split()
    fruits = [int(x) for x in fruits]
    fruits = [x*x for x in fruits]
    print(fruits)
</code>
<|/ a |>
<| c |>
Thank you very much! I 