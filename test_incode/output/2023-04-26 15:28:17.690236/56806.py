#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port and prints a list of words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(1, port+1):
        words.append(str(i))
    print('\n'.join(words))
</code>
<|/ a |>
<| c |>
Thanks for your answer, but i don't think this answers my question. My question is how to print a list of numbers, not a list of words. I edited my question to clarify this.
<|/ c |>
<| c |>
Oh ok, i see. So you want to print a list of numbers, not a list of words. I edited my answer to show you how to do that. Let me know if that works for you.
<|/ c |>
<| c |>
Thanks for your answer, but i don't think this answers my question. My question is how to print a list of numbers, not a list of words. I edited my question to clarify this.
<|/ c |>
<| c |>
Oh ok, i see. So you want to print a list of numbers, not a list of words. I edited my answer to show you how to do that. Let me know if that works for you.
<|/ c |>
<| c |>
Thanks for your answer, but i don't think this answers my question. My question is how to print a list of numbers, not a list of words. I edited my question to clarify this.
<|/ c |>
<| a dscore=0 |>
<code>
def printWords(n):
    words = []
    for i in range(1, n+1):
        words.append(str(i))
    return words

print(printWords(5))
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thanks for your answer, but i don't think this answers my question. My question is how to print a list of numbers, not a list of words. I edited my question to clarify this.
<|/ c |>
<| a tags=python,python-3.x dscore=0 |>
<code>
def printWords(n):
    words = []
    for i in range(1, n+1):
        words.append(str(i))
    return words

print(printWords(5))
</code>
<|/ a |>
<| c |>
Thanks for your answer, but i don't think this answers my question. My question is how to print a list of numbers, not a list of words. I edited my question to clarify this.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def printWords(n):
    words = []
    for i in range(1, n+1):
        words.append(str(i))
    return words

print(printWords(5))
</code>
<|/ a dscore