#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and returns a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = []
    while True:
        fruits_copy = list(fruits)
        fruits_copy.remove('apple')
        fruits_copy.remove('banana')
        fruits_copy.remove('cherry')
        words.append(' '.join(fruits_copy))
        if fruits_copy == []:
            break
    print(words)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the answer. I'm still trying to figure out how this works, but I appreciate it.
<|/ c |>
<| c |>
This code will keep running until you exit the program (ctrl+c), then it will print out the words. If you want it to stop after you finish iterating over all the fruits, you can add `break` after `words.append(' '.join(fruits_copy))`
<|/ c |>
<| c |>
Thanks again! I appreciate it!
<|/ c |>
<| c |>
No problem! If this answered your question, please mark it as accepted so others can see that this question has been answered.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
words = []
while True:
    fruits_copy = list(fruits)
    fruits_copy.remove('apple')
    fruits_copy.remove('banana')
    fruits_copy.remove('cherry')
    words.append(' '.join(fruits_copy))
    if fruits_copy == []:
        break
print(words)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the answer. I'm still trying to figure out how this works, but I appreciate it.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
words = []
while True:
    fruits_copy = list(fruits)
    fruits_copy.remove('apple')
    fruits_copy.remove('banana')
    fruits_copy.remove('cherry')
    words.append(' '.join(fruits_copy))
    if fruits_copy == []:
        break
print(words)
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
words = []
while True:
    fruits_copy = list(fruits)
    fruits_copy.remove('apple')
    fruits_