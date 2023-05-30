#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse']
    enumerated_words = []
    for index, word in enumerate(words):
        enumerated_words.append(word)
        if index == 3:
            break
    print(enumerated_words)
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>
<| c |>
Glad I could help. If this answer helped you solve your problem, please consider accepting it by clicking the green check mark to the left of the answer.
<|/ c |>
<| c |>
Yes, it did! Thank you very much!
<|/ c |>
<| a dscore=0 |>
<code>
words = ['cat', 'dog', 'mouse']
for index, word in enumerate(words):
    if index == 3:
        break
    print(word)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>