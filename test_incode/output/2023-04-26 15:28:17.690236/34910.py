#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words[-1] == 'q':
            break
    print('\n'.join(words))
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| c |>
I did it but when I type "q" it just closes the program. How do I make it keep running?
<|/ c |>
<| c |>
I edited the answer to include a while loop that will keep asking until the user enters "q" 