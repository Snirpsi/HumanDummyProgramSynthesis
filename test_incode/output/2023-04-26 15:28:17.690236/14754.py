#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts fruits and adds numbers. """    
    fruits = ("apple", "banana", "cherry")
    numbers = ("1", "2", "3")
    fruits_number = []
    numbers_number = []
    for fruit in fruits:
        fruits_number.append(fruit)
    for number in numbers:
        numbers_number.append(number)
    fruits_number.append("Total")
    numbers_number.append("Total")
    print(" ".join(fruits_number))
    print(" ".join(numbers_number))
</code>
<|/ a |>
<| c |>
Thank you so much! This was exactly what I needed!
<|/ c |>
<| c |>
You're welcome. Don't forget to accept the answer if it helped you.
<|/ c |>
<| c |>
I did but my reputation isn't high enough to do so. Thanks again!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
I noticed that when I run this code, it prints out the total of the fruits twice. Is there a way to get it to print out the total only once and only once?
<|/ c |>
<| a tags=python-3.x,python |>
<code>
fruits = ("apple", "banana", "cherry")
numbers = ("1", "2", "3")
fruits_number = []
numbers_number = []
for fruit in fruits:
    fruits_number.append(fruit)
for number in numbers:
    numbers_number.append(number)
fruits_number.append("Total")
numbers_number.append("Total")
print(" ".join(fruits_number))
print(" ".join(numbers_number))
</code>
<|/ a dscore=0 |>
<| c |>
This code doesn't add `Total` to the end of each list
<|/ c |>
<| c |>
I noticed that when I run this code, it prints out the total of the fruits twice. Is there a way to get it to print out the total only once and only once?
<|/ c |>
<| c |>
I noticed that when I run this code, it prints out the total of the fruits twice. Is there a way to get it to print out the total only once and only once?
<|/ c |>
<| c |>
I noticed that when I run this code, it prints out the total of the fruits twice. Is there a way to get it to print out the total only once and only once?
<|/ c |>
<| c |>
I noticed that when I run this code, it 