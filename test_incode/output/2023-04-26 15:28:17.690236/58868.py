#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and converts fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_converted = []
    while True:
        fruits_converted.append(fruits.pop(0))
        print('Converted fruits: ', fruits_converted)
        time.sleep(1)
</code>
<|/ a |>
<| c |>
Thanks for your answer, but I don't think this would work as I intended it to work. I'm looking to convert a list of fruits into a list of numbers, not strings. So the output would look like [1,2,3,4,5,6,7,8,9,10,11,12]
<|/ c |>
<| c |>
Yes, I understand that. I'll edit the answer to show you how to do that.
<|/ c |>
<| c |>
Thanks so much! This worked perfectly!
<|/ c |>
<| a dscore=0 tags=python-3.x,python |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_converted = []
while True:
    fruits_converted.append(fruits.pop(0))
    print('Converted fruits: ', fruits_converted)
    time.sleep(1)
</code>
<|/ a |>
<| c |>
Thanks for your answer, but I don't think this would work as I intended it to work. I'm looking to convert a list of fruits into a list of numbers, not strings. So the output would look like [1,2,3,4,5,6,7,8,9,10,11,12]
<|/ c |>
<| c |>
It would work if you used `int()`, but that would convert it to a string. `int()` will convert it to a number, so `int('banana')` will give `2`.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_converted = []
while True:
    fruits_converted.append(fruits.pop(0))
    print('Converted fruits: ', fruits_converted)
    time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer, but I don't think this would work as I intended it to work. I'm looking to convert a list of fruits into a list of numbers, not strings. So the output would look like [1,2,3,4,5,6,7,8,9,10,11,12]
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits_converted = []
while True:
    fruits_converted.append(fruits.pop(0))
    print('Converted fruits: ', fruits_converted)