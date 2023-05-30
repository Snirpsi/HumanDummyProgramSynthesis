#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == 'q':
            break
    print(" ".join(words))
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. I'm new to python and I didn't know that you could use a while loop to store words. I understand that I can use input() to store words. But what if I want to store words in a list? I tried to do that but it didn't work. Could you please show me how to do that?
<|/ c |>
<| c |>
I added an example to my answer.
<|/ c |>
<| c |>
Thank you for your help. I appreciate it.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
If this answer helped you, please consider accepting it: https://stackoverflow.com/help/someone-answers
<|/ c |>
<| a dscore=0 |>
<code>
words = []
while True:
    words.append(input("Enter a word: "))
    if words[-1] == 'q':
        break
print(" ".join(words))
</code>
<|/ a tags=python |>
<| c |>
Thank you for your answer. I'm new to python and I didn't know that you could use a while loop to store words. I understand that I can use input() to store words. But what if I want to store words in a list? I tried to do that but it didn't work. Could you please show me how to do that?
<|/ c |>
<| c |>
I added an example to my answer.
<|/ c |>
<| a tags=python |>
<code>
words = []
while True:
    words.append(input("Enter a word: "))
    if words[-1] == 'q':
        break
print(" ".join(words))
</code>
<|/ a dscore=0 |>
<| c |>
Thank you for your answer. I'm new to python and I didn't know that you could use a while loop to store words. I understand that I can use input() to store words. But what if I want to store words in a list? I tried to do that but it didn't work. Could you please show me how to do that?
<|/ c |>
<| c |>
I added an example to my answer.
<|/ c |>
<| a tags=python |>
<code>
words = []
while True:
    words.append(input("Enter a word: "))
    if words[-1] == 'q':
        break
print(" ".join(words))
</code>
<|/ a dscore=0 |>