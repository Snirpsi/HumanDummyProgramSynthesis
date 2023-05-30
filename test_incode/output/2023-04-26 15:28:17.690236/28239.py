#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and removes user input. """    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        words.append(word)
    print("\n".join(words))
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This works perfectly. Thank you!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def word_list(words):
    words_list = []
    for word in words:
        words_list.append(word)
    return words_list

words_list = word_list(["hello", "world", "how", "are", "you", "today"])
print(words_list)
</code>
<|/ a dscore=0 |>
<| c |>
This works perfectly. Thank you!
<|/ c |>
<| a dscore=0 |>
<code>
def word_list(words):
    words_list = []
    for word in words:
        words_list.append(word)
    return words_list

words_list = word_list(["hello", "world", "how", "are", "you", "today"])
print(words_list)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
This works perfectly. Thank you!
<|/ c |>