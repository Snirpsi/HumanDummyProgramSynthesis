#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    for word in open('words.txt'):
        words.append(word.rstrip())
    return words
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for the answer. I'm new to python, so I didn't know about this function. I'll try it out and see how it goes.
<|/ c |>
<| c |>
Yes, it works. I used this as a template to build my own functions. Thanks again!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
One more question, how would I go about making this function so that it prints out the words in the file "words.txt" that have the word "dog" in the first column? I tried putting in "dog" in the first column but that didn't work.
<|/ c |>
<| c |>
I added a line to my answer that does that. Let me know if that works for you.
<|/ c |>
<| a dscore=0 |>
<code>
def words_in_file(filename):
    words = []
    with open(filename) as f:
        for line in f:
            words = words + line.strip().split()
    return words
</code>
<|/ a tags=python |>
<| c |>
Thanks for the answer. I'm new to python, so I didn't know about this function. I'll try it out and see how it goes.
<|/ c |>
<| a tags=python |>
<code>
def words_in_file(filename):
    words = []
    with open(filename) as f:
        for line in f:
            words = words + line.strip().split()
    return words
</code>
<|/ a dscore=0 |>