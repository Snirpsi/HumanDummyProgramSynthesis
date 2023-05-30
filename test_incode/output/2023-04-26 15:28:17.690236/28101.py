#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    wordlist = open('words.txt', 'r')
    for line in wordlist:
        print(line.rstrip())
    wordlist.close()
</code>
<|/ a tags=python,python-3.x dscore=0 |>
<| c |>
This doesn't work because `wordlist` is already a file object so `for line in wordlist` will iterate over it twice.
<|/ c |>
<| c |>
Yes, I know. My answer was intended to be a general solution to the problem. I'll edit my answer to include a more general solution.
<|/ c |>
<| c |>
I edited my answer to include a more general solution. Hope this helps.
<|/ c |>
<| c |>
Thank you for the solution! It works perfectly now!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>