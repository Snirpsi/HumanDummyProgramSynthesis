#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    return words
</code>
<|/ a dscore=0 tags=python |>
<| c |>
Thanks for the help. I did what you suggested but now I'm getting this error: Traceback (most recent call last):
  File "words.py", line 4, in <module>
    with open('words.txt', 'r') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'words.txt'
<|/ c |>
<| c |>
Okay, I figured it out. I had to change the line to 'with open(file) as file'
<|/ c |>
<| c |>
Yes, I forgot to change that too.
<|/ c |>
<| c |>
Yes, I forgot to change that too.
<|/ c |>
<| c |>
Thanks so much! I appreciate it!
<|/ c |>