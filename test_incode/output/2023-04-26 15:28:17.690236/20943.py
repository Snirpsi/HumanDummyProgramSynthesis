#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words. """    
    while True:
        words = []
        with open('words.txt', 'r') as f:
            for line in f:
                words.append(line.strip())
        for word in words:
            print(word)
        time.sleep(1)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
It does. I didn't realize that OP wanted to read from a text file
<|/ c |>
<| c |>
Yes, I realize that and I edited my answer to reflect that
<|/ c |>
<| c |>
Thanks, this was very helpful
<|/ c |>
<| c |>
I added a version that reads from a text file
<|/ c |>
<| a dscore=0 |>
<code>
import fileinput
for line in fileinput.input():
    print(line)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| a dscore=0 |>
<code>
with open('words.txt', 'r') as f:
    for line in f:
        print(line)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| a tags=python-3.x,python |>
<code>
with open('words.txt', 'r') as f:
    for line in f:
        print(line)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| a dscore=0 |>
<code>
with open('words.txt', 'r') as f:
    for line in f:
        print(line)
</code>
<|/ a tags=python-3.x,python |>
<| a tags=python-3.x,python |>
<code>
with open('words.txt', 'r') as f:
    for line in f:
        print(line)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't answer the question
<|/ c |>
<| c |>
This doesn't answer the question
<|/ c |>
<| a dscore=0 |>
<code>
with open('word