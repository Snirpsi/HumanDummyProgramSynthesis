#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    while True:
        fruits = ['apple', 'orange', 'banana', 'cherry']
        fruits.append(fruits.pop(0))
        print(fruits)
        time.sleep(1)
</code>
<|/ a |>
<| c |>
This works perfectly, thank you!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
fruits = ['apple', 'orange', 'banana', 'cherry']
while len(fruits) != 0:
    fruits.pop(0)
    print(fruits)
    time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>
<| a |>
<code>
fruits = ['apple', 'orange', 'banana', 'cherry']
while len(fruits) != 0:
    fruits.pop(0)
    print(fruits)
    time.sleep(1)
</code>
<|/ a tags=python-3.x,python dscore=0 |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>