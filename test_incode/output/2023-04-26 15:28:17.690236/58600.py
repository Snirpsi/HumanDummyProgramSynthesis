#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and stores a list of words. """    
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.split()
    numbers = list(filter(None, numbers))
    words = []
    while numbers:
        words.append(numbers.pop(0))
    print(words)
</code>
<|/ a tags=python-3.x,python,list |>
<| c |>
This code will remove all numbers from the list. OP wants to remove all words from the list.
<|/ c |>
<| c |>
Yes, I know, but I thought it would be a good idea to show him how to remove all words from the list. He can just remove the `while` loop and replace `numbers = list(filter(None, numbers))` with `numbers = list(filter(None, numbers)).split()`
<|/ c |>
<| c |>
I see. Thanks for your help!
<|/ c |>
<| c |>
No problem. Glad I could help!
<|/ c |>
<| a tags=python-3.x,python,list |>
<code>
numbers = input("Enter a list of numbers: ")
numbers = numbers.split()
numbers = list(filter(None, numbers))
words = []
for number in numbers:
    words.append(number)
print(words)
</code>
<|/ a dscore=0 |>
<| c |>
This code will remove all numbers from the list. OP wants to remove all words from the list.
<|/ c |>
<| a tags=python-3.x,python,list |>
<code>
numbers = input("Enter a list of numbers: ")
numbers = numbers.split()
numbers = list(filter(None, numbers))
words = []
for number in numbers:
    words.append(number)
print(words)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
<code>
numbers = input("Enter a list of numbers: ")
numbers = numbers.split()
numbers = list(filter(None, numbers))
words = []
for number in numbers:
    words.append(number)
print(words)
</code>
<|/ a tags=python-3.x,python,list |>
<| a |>
<code>
numbers = input("Enter a list of numbers: ")
numbers = numbers.split()
numbers = list(filter(None, numbers))
words = []
for number in numbers:
    words.append(number)
print(words)
</code>
<|/ a dscore=0 tags=python-3.x,python,list |>
<| a tags=python-3.x,python,list |>
<code>
numbers = input("Enter a list of numbers: ")
numbers = numbers.split()
numbers = list(filter(None, numbers))
words = []
for number in numbers:
    words.append(