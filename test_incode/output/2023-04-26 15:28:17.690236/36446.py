#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == "":
            break
    print(words)
</code>
<|/ a dscore=1 |>
<| c |>
This works perfectly, thank you! I 