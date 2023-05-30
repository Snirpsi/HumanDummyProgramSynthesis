#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    print(words)
</code>
<|/ a |>
<| c |>
Thanks for the answer. Can you explain to me what does this line do? `line = line.strip()`
<|/ c |>
<| c |>
`line = line.strip()` strips leading and trailing whitespace from the line and replaces it with an empty string.
<|/ c |>
<| c |>
Thanks so much! 