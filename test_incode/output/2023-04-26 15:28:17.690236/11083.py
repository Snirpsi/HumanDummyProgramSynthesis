#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words. """    
    words = []
    for word in open('words.txt'):
        words.append(word.strip())
    return words
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| c |>
Thank you very much! This was exactly what I was looking for.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
Hi again, I have another question. How can I make the program print out the words that do not contain 'a' and 'b'? I tried adding 'if word not in ['a', 'b']' but that did not work.
<|/ c |>
<| c |>
I edited my answer to show how to do that. Glad I could help.
<|/ c |>
<| c |>
Thank you very much! I really appreciate your help.
<|/ c |>
<| a dscore=0 |>
<code>
words = []
with open('words.txt') as file:
    for line in file:
        words.append(line.strip())
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you very much! This was exactly what I was looking for.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
with open('words.txt') as file:
    words = [word.strip() for word in file]
</code>
<|/ a dscore=0 |>