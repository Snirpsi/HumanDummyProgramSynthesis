#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and iterates over words. """    
    words_to_remove = input("Enter the words to remove: ")
    words_to_remove = words_to_remove.split()
    for word in words_to_remove:
        if word in words:
            words.remove(word)
        else:
            print("The word %s is not in the dictionary." % word)
    print("The words have been removed from the dictionary.")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help. I really appreciate it!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
Can you please help me with one more thing? I want the program to ask the user for an input and then remove that word from the dictionary. How would I do that?
<|/ c |>
<| c |>
I added the code to do that. Let me know if that helps.
<|/ c |>
<| c |>
Thanks so much! I really appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
words_to_remove = input("Enter the words to remove: ")
words_to_remove = words_to_remove.split()
for word in words_to_remove:
    if word in words:
        words.remove(word)
    else:
        print("The word %s is not in the dictionary." % word)
print("The words have been removed from the dictionary.")
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks so much for your help. I really appreciate it!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
words_to_remove = input("Enter the words to remove: ")
words_to_remove = words_to_remove.split()
for word in words_to_remove:
    if word in words:
        words.remove(word)
    else:
        print("The word %s is not in the dictionary." % word)
print("The words have been removed from the dictionary.")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help. I really appreciate it!
<|/ c |>
<| a tags=python-3.x,python |>
<code>
words_to_remove = input("Enter the words to remove: ")
words_to_remove = words_to_remove.split()
for word in words_to_remove:
    if word in words:
        words.remove(word)
    else:
        print("The word %s is not in the dictionary." % word)
print("The words have been removed from the dictionary.")
</code>
<|/ a dscore=0 |>
<| c |>
Thanks so much for your help. I really appreci