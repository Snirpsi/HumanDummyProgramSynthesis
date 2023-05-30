#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or enumerates words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    print('\n'.join(words))
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much! This helped me a lot!
<|/ c |>
<| c |>
