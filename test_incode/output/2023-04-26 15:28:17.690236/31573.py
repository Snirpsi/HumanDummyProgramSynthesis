#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    words = []
    for word in open('words.txt'):
        words.append(word.strip())
    print(words)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could do that with 'open'. I will try it out and see if it works.
<|/ c |>
<| c |>
No problem! I added a little more explanation to the answer, hope it helps.
<|/ c |>
<| c |>
Thanks, it works. I added the 'with' statement and now it works fine.
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| a |>
You don't need open() at all.
<code>
with open('words.txt') as words:
    words = [word.strip() for word in words]
</code>
<|/ a tags=python,python-3.x dscore=0 |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could do that with 'open'. I will try it out and see if it works.
<|/ c |>
<| c |>
No problem! I added a little more explanation to the answer, hope it helps.
<|/ c |>
<| a dscore=0 |>
<code>
with open('words.txt') as words:
    words = [word.strip() for word in words]
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could do that with 'open'. I will try it out and see if it works.
<|/ c |>
<| a dscore=0 |>
<code>
with open('words.txt') as words:
    words = [word.strip() for word in words]
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you could do that with 'open'. I will try it out and see if it works.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
with open('words.txt') as words:
    words = [word.strip() for word in words]
</code>
<|/ a dscore=0 |>
<| a tags=python,python-3.x |>
<code>
with open('words.txt') as words:
    words = [word.strip() for word in words]
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I'm 