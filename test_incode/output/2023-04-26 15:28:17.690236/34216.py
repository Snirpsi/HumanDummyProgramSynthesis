#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words. """    
    words = []
    for word in open('words.txt').read().split():
        words.append(word)
    for word in words:
        print(word)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. 