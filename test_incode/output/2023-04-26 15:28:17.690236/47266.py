#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and returns fruits. """    
    fruits = []
    while True:
        fruits.append(get_fruit())
        print('Fruits: ', fruits)
        time.sleep(1)
</code>
<|/ a |>
<| c |>
Thank you very much! This was exactly what I was looking for!
<|/ c |>
<| c |>
You're welcome. Glad I could help.
<|/ c |>
<| c |>
This code will hang forever if you run it in a terminal. Try running it in a script and see if it hangs.
<|/ c |>
<| c |>
Thanks for the heads up. I've edited the answer to include a script that runs the code in a terminal and doesn't hang.
<|/ c |>
<| c |>
Thanks again! This was exactly what I was looking for!
<|/ c |>
<| a dscore=0 tags=python,python-3.x |>
This code will hang forever if you run it in a terminal. Try running it in a script and see if it hangs.
<code>
import time

def get_fruit():
    """ Returns a random fruit from the list. """
    fruits = ['apple', 'banana', 'cherry']
    return random.choice(fruits)

if __name__ == '__main__':
    while True:
        fruit = get_fruit()
        print('Fruit: ', fruit)
        time.sleep(1)
</code>
<|/ a |>
<| c |>
Thanks for the heads up. I've edited the answer to include a script that runs the code in a terminal and doesn't hang.
<|/ c |>
<| c |>
Thanks again! This was exactly what I was looking for!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
Thanks again! This was exactly what I was looking for!
<|/ c |>
<| a dscore=0 tags=python,python-3.x |>
This code will hang forever if you run it in a terminal. Try running it in a script and see if it hangs.
<code>
import time

def get_fruit():
    """ Returns a random fruit from the list. """
    fruits = ['apple', 'banana', 'cherry']
    return random.choice(fruits)

if __name__ == '__main__':
    while True:
        fruit = get_fruit()
        print('Fruit: ', fruit)
        time.sleep(1)
</code>
<|/ a |>
<| c |>
Thanks for the heads up. I've edited the answer to include a script that runs the code in a terminal and doesn't hang.
<|/ c |>
<| c |>