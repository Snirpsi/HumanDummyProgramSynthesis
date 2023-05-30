#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and converts fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_number = enumerate(fruits)
    fruits_number = [fruit for fruit in fruits_number if fruit[1] > 0]
    print(fruits_number)
</code>
<|/ a |>
<| c |>
This code doesn't work. `fruits_number` only has one element, and `fruit[1]` is an index error. `fruits_number[0]` works.
<|/ c |>
<| c |>
Thanks for the feedback. Updated.
<|/ c |>
<| c |>
Thanks so much for your help. I really appreciate it!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_number = [fruit for fruit in fruits if fruit[1] > 0]
print(fruits_number)
</code>
<|/ a dscore=0 tags=python,python-3.x |>
<| c |>
This code doesn't work. `fruits_number` only has one element, and `fruit[1]` is an index error. `fruits_number[0]` works.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_number = [fruit for fruit in fruits if fruit[1] > 0]
print(fruits_number)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This code doesn't work. `fruits_number` only has one element, and `fruit[1]` is an index error. `fruits_number[0]` works.
<|/ c |>
<| a dscore=0 tags=python,python-3.x |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_number = [fruit for fruit in fruits if fruit[1] > 0]
print(fruits_number)
</code>
<|/ a |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_number = [fruit for fruit in fruits if fruit[1] > 0]
print(fruits_number)
</code>
<|/ a tags=python,python-3.x |>
<| a |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_number = [fruit for fruit in fruits if fruit[1] > 0]
print(fruits_number)
</code>
<|/ a 