#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits and iterates over words. """    
    fruits = open('fruits.txt', 'r')
    words = fruits.read().split()
    for word in words:
        print(word)
    fruits.close()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much! I appreciate your help!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
I did it but now I get the error: TypeError: expected str, bytes or os.PathLike object, not list
<|/ c |>
<| c |>
Oh I see, I forgot to add the .split() to the words variable. I've edited my answer to reflect this.
<|/ c |>
<| c |>
Thanks so much! I appreciate your help!
<|/ c |>