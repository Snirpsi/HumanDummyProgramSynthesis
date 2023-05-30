#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words and removes numbers. """    
    words = input("Enter the words: ").split()
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in "0123456789"]
    print(" ".join(words))
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your help! It works perfectly now!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def removeNumbers(word):
    word = word.replace(",", "")
    word = word.replace("-", "")
    word = word.replace("_", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("'", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace("!