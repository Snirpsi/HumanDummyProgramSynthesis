#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and removes a port. """    
    wordlist = open('wordlist.txt').read().splitlines()
    wordlist = [word for word in wordlist if word not in open('ports.txt').read().splitlines()]
    open('wordlist.txt', 'w').writelines(wordlist)
    open('ports.txt', 'w').writelines(open('wordlist.txt').read().splitlines())
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help! I really appreciate it!
<|/ c |>
<| c |>
You're welcome. Don't forget to accept the answer if it helped you.
<|/ c |>
<| c |>
