#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words or enumerates a list of words. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        if word != '':
            words.append(word)
    print(words)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I've tried your code, but it still doesn't work. I'm wondering if there's something wrong with my python version or my operating system. I've tried it on python 3.7.3 and it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| c |>
I tested it on python 3.7.3 and it works. I updated my answer with a working example.
<|/ c |>
<| c |>
Thanks for your reply. I've tried it on my computer but it still doesn't work. I've tried it on python 3.7.3 and it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| c |>
I tested it on python 3.7.3 and it works. I updated my answer with a working example.
<|/ c |>
<| c |>
Thanks for your reply. I've tried it on my computer but it still doesn't work. I've tried it on python 3.7.3 and it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| a tags=python-3.x,python |>
The code below will print all words in the text file as they appear in the text file.
<code>
with open('words.txt', 'r') as file:
    for line in file:
        print(line)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I've tried your code, but it still doesn't work. I'm wondering if there's something wrong with my python version or my operating system. I've tried it on python 3.7.3 and it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| c |>
The code above is working fine on my computer. Are you sure the file words.txt exists?
<|/ c |>
<| c |>
Yes, it does exist. I've tried it on my computer but it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| c |>
I tested it on my computer but it still doesn't work. I've tried it on python 3.7.3 and it still doesn't work. Do you think there's something wrong with my operating system?
<|/ c |>
<| c |>
I tested it on my computer but it still doesn't work. I've tried 