#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A program that converts a list of words.
    #The program will ask the user for a word and print it out
    #in reverse order.
    wordlist = input("Enter a word: ")
    wordlist = wordlist.split()
    wordlist.sort(reverse = True)
    for word in wordlist:
        print(word)
</code>
<|/ a tags=python-3.x,python |>
<| c |>
This doesn't work. `wordlist` isn't a list, it's a string. `wordlist.split()` doesn't do what you think it does.
<|/ c |>
<| c |>
Yes it does. `wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| c |>
`wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| c |>
`wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| c |>
`wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
wordlist = input("Enter a word: ")
wordlist = wordlist.split()
wordlist.sort(reverse = True)
for word in wordlist:
    print(word)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work. `wordlist` isn't a list, it's a string. `wordlist.split()` doesn't do what you think it does.
<|/ c |>
<| c |>
Yes it does. `wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| c |>
`wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| c |>
`wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| a tags=python-3.x,python |>
<code>
wordlist = input("Enter a word: ")
wordlist = wordlist.split()
wordlist.sort(reverse = True)
for word in wordlist:
    print(word)
</code>
<|/ a dscore=0 |>
<| c |>
This doesn't work. `wordlist` isn't a list, it's a string. `wordlist.split()` doesn't do what you think it does.
<|/ c |>
<| c |>
Yes it does. `wordlist.split()` splits the string into words. `wordlist` is a list of words. `wordlist.sort()` sorts the words in `wordlist`. `reverse=True` reverses the order of the words. `for word in wordlist` iterates over each word in `wordlist`. `print(word)` prints the word in the order it was entered.
<|/ c |>
<| a |>
<code>
wordlist = input("Enter a word: ")
wordlist = wordlist.split()
wordlist.sort(reverse = True)
for word in wordlist:
    print(word)
</code>
<|/ a dscore=0 tags=python-3.x,python |>
<| a dscore=0 |>
<code>
wordlist = input("Enter a word: ")
wordlist = wordlist.split()
wordlist.sort(reverse = True)
for word in wordlist:
    print(word)
</code>
<|/ a tags=python-3.x,python |>
