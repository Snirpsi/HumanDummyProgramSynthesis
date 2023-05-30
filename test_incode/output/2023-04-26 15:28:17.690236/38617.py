#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and prints a list of words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    print(words)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! It worked! :)
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| c |>
