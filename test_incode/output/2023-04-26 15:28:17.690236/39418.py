#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print('Adding ' + fruit)
        fruits.append(fruit)
    print('Done')
</code>
<|/ a |>
<| c |>
Thanks for the answer! I appreciate it!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
I added a little more explanation to the answer.
<|/ c |>
<| c |>
Thanks again! I appreciate it!
<|/ c |>
<| a dscore=0 tags=python,list,python-3.x |>
You can use a list comprehension:
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [fruit for fruit in fruits if fruit != 'apple']
</code>
<|/ a |>
<| c |>
Thanks for the answer! I appreciate it!
<|/ c |>
<| a dscore=0 tags=python,list,python-3.x |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a tags=python,list,python-3.x |>
<| a tags=python,list,python-3.x |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a dscore=0 |>
<| a |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a tags=python,list,python-3.x dscore=0 |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a tags=python,list,python-3.x |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a tags=python,list,python-3.x |>
<| a tags=python,list,python-3.x dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
fruits = [x for x in fruits if x != 'apple']
</code>
<|/ a |>
<|