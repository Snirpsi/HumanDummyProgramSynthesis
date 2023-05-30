#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits or prints a list of words. """    
    fruit = input("Enter a fruit: ")
    fruits = fruit.split()
    for fruit in fruits:
        print(fruit)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for the answer. Could you please explain to me what does "fruits = fruit.split()" do?
<|/ c |>
<| c |>
`fruits = fruit.split()` splits the string `fruit` into its individual characters. So `fruit = 'bananas'` would become `fruits = ['a', 'n', 'n', 'a', 'n', 'a', 'n']`
<|/ c |>
<| c |>
Thank you very much. Now I understand.
<|/ c |>
<| a dscore=0 |>
<code>
fruit = 'bananas'
fruits = fruit.split()
print(fruits)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Please add some explanation to your answer
<|/ c |>
<| a dscore=0 |>
<code>
fruit = 'bananas'
fruits = fruit.split()
print(fruits)
</code>
<|/ a tags=python,python-3.x |>
<| a tags=python,python-3.x |>
<code>
fruit = 'bananas'
fruits = fruit.split()
print(fruits)
</code>
<|/ a dscore=0 |>