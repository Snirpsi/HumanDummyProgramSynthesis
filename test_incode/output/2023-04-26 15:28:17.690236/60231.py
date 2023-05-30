#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits. """    
    fruits = ["apple", "banana", "cherry"]
    fruits_sum = 0
    for fruit in fruits:
        fruits_sum += fruit
    print(fruits_sum)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This answer is not correct. `sum` does not mutate the list in-place, it returns a new list with the sum of the original list. `fruits_sum = sum(fruits)` will mutate the list in-place.
<|/ c |>
<| c |>
: Thanks for pointing that out. Fixed the answer.
<|/ c |>
<| c |>
: Thanks for the correction. Updated the answer.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a tags=python-3.x,python |>
<| a tags=python-3.x,python |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a dscore=0 |>
<| a |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_sum = 0
for fruit in fruits:
    fruits_sum += fruit
print(fruits_sum)
</code>
<|/ a tags=python-3.x,python |>