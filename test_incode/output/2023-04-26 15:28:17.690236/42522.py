#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits. """    
    fruits = ["apple", "banana", "cherry"]
    fruits_multiplied = [0] * len(fruits)
    for fruit in fruits:
        fruits_multiplied[fruit.lower()] = int(fruit.lower()) * 3
    print(fruits_multiplied)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer! I didn't know about `map` before. I'll try it out and see how it works.
<|/ c |>
<| c |>
The code works perfectly fine now! Thanks so much!
<|/ c |>
<| c |>
You're welcome! If it solved your problem, please consider marking it as the accepted answer.
<|/ c |>
<| c |>
I did, but it says I have to wait a couple of minutes. I'll do it when I can.
<|/ c |>
<| c |>
Okay, I added the code to the answer. Glad I could help.
<|/ c |>
<| a tags=python |>
You could use list comprehension:
<code>
fruits = ["apple", "banana", "cherry"]
fruits_multiplied = [int(fruit.lower()) * 3 for fruit in fruits]
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer! I didn't know about `map` before. I'll try it out and see how it works.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_multiplied = [int(fruit.lower()) * 3 for fruit in fruits]
</code>
<|/ a tags=python |>
<| c |>
Thanks for the answer! I didn't know about `map` before. I'll try it out and see how it works.
<|/ c |>
<| a tags=python |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_multiplied = [int(fruit.lower()) * 3 for fruit in fruits]
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_multiplied = [int(fruit.lower()) * 3 for fruit in fruits]
</code>
<|/ a tags=python |>
<| a |>
<code>
fruits = ["apple", "banana", "cherry"]
fruits_multiplied = [int(fruit.lower()) * 3 for fruit in fruits]
</code>
<|/ a dscore=0 tag