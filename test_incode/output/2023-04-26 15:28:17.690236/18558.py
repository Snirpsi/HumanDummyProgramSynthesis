#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    fruits = open('fruits.txt', 'r')
    while True:
        fruit = fruits.readline()
        if fruit == '':
            break
        fruit = fruit.strip()
        fruits = open('fruits.txt', 'w')
        fruits.write(fruit)
        fruits.close()
    print('Done')
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I am new to python and still learning how to use it. Your code works perfectly. Thanks again.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
fruits = open('fruits.txt', 'r')
while True:
    fruit = fruits.readline()
    if fruit == '':
        break
    fruit = fruit.strip()
    fruits = open('fruits.txt', 'w')
    fruits.write(fruit)
    fruits.close()
print('Done')
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I am new to python and still learning how to use it. Your code works perfectly. Thanks again.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = open('fruits.txt', 'r')
while True:
    fruit = fruits.readline()
    if fruit == '':
        break
    fruit = fruit.strip()
    fruits = open('fruits.txt', 'w')
    fruits.write(fruit)
    fruits.close()
print('Done')
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I am new to python and still learning how to use it. Your code works perfectly. Thanks again.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = open('fruits.txt', 'r')
while True:
    fruit = fruits.readline()
    if fruit == '':
        break
    fruit = fruit.strip()
    fruits = open('fruits.txt', 'w')
    fruits.write(fruit)
    fruits.close()
print('Done')
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I am new to python and still learning how to use it. Your code works perfectly. Thanks again.
<|/ c |>