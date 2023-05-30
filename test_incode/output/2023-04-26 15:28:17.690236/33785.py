#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words and adds user input. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == "":
            break
    print(" ".join(words))
</code>
<|/ a dscore=0 tags=python,python-3.x |>
<| c |>
Thank you very much for your help! I appreciate it!
<|/ c |>
<| a |>
You can use a while loop to keep asking the user for input, and break the loop when they enter an empty string:
<code>
while True:
    words.append(input("Enter a word: "))
    if words[-1] == "":
        break
</code>
<|/ a tags=python,python-3.x dscore=0 |>
<| c |>
Thank you very much for your help! I appreciate it!
<|/ c |>
<| a |>
<code>
words = []
while True:
    words.append(input("Enter a word: "))
    if words[-1] == "":
        break
print(" ".join(words))
</code>
<|/ a dscore=0 tags=python,python-3.x |>
<| c |>
Thank you very much for your help! I appreciate it!
<|/ c |>
<| a |>
<code>
words = []
while True:
    words.append(input("Enter a word: "))
    if words[-1] == "":
        break
print(" ".join(words))
</code>
<|/ a dscore=0 tags=python,python-3.x |>