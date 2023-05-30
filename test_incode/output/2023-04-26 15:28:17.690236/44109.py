#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and stores numbers. """    
    words = ['cat', 'dog', 'bird', 'cat', 'dog', 'bird', 'cat', 'dog', 'bird', 'cat', 'dog', 'bird']
    numbers = []
    for word in words:
        numbers.append(word.count('dog'))
    print(numbers)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| a dscore=0 |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| c |>
Glad it helped!
<|/ c |>
<| a dscore=0 |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
</code>
<|/ a dscore=0 |>
<| a |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
</code>
<|/ a tags=python-3.x,python dscore=0 |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| a dscore=0 |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
</code>
<|/ a tags=python-3.x,python |>
<| a dscore=0 |>
<code>
def count_dogs(words):
    counts = {}
    for word in words:
        if word in counts:
            count