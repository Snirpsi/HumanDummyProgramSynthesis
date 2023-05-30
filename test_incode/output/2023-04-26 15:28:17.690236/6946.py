#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and prints all ports. """    
    words = []
    ports = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
        ports.append(get_port(word))
    print('\n'.join(words))
    print('\n'.join(ports))
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This code doesn't work. Try entering 'q' instead of 'exit' and you'll see that it prints nothing. Also, the `get_port` function doesn't work either. Try entering 'exit' instead of 'q' and you'll see that it prints nothing.
<|/ c |>
<| c |>
I fixed the get_port function and added a while loop to keep asking the user for input until they enter 'q'.
<|/ c |>
<| c |>
This code doesn't work either. Try entering 'q' instead of 'exit' and you'll see that it prints nothing. Also, the `get_port` function doesn't work either. Try entering 'exit' instead of 'q' and you'll see that it prints nothing.
<|/ c |>
<| c |>
It works fine for me on Python 3.6.3. What version of Python are you using?
<|/ c |>
<| c |>
I'm using Python 3.6.3. I tried entering 'exit' instead of 'q' and it still prints nothing.
<|/ c |>
<| a dscore=0 |>
<code>
