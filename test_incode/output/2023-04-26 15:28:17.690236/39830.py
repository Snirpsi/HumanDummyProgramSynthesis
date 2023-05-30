#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'q':
            break
    print(words)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. Your code works perfectly for me, but I still don't understand how it works. Can you explain it to me?
<|/ c |>
<| c |>
I added some comments to my answer explaining what each line does.
<|/ c |>
<| c |>
Thanks a lot! I understood it now. 