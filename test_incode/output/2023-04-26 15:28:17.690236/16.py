#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and removes numbers. """    
    wordlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    wordlist = [word.lower() for word in wordlist]
    wordlist = [word for word in wordlist if word.isdigit()]
    print(wordlist)
</code>
<|/ a tags=python,python-3.x |>
<| a tags=python,python-3.x |>
<code>
def remove_digits(word):
    word=str(word)
    word=word.replace(',','')
    word=word.replace('.','')
    word=word.replace('-','')
    word=word.replace(' ','')
    word=word.replace('\n','')
    word=word.replace('\r','')
    word=word.replace('\t','')
    word=word.replace('