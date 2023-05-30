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
<|/ a tags=python,python-3.x |>
<| c |>
Thank you so much! This helped me a lot!
<|/ c |>
<| c |>
You're welcome. Don't forget to mark the answer as accepted if it helped you. :)
<|/ c |>
<| c |>
