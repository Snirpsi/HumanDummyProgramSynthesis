#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words and multiplyes user input. """    
    wordlist = input("Enter a word: ")
    wordlist = wordlist.split()
    wordlist = [int(word) for word in wordlist]
    wordlist = [wordlist[i]*wordlist[i+1] for i in range(len(wordlist)-1)]
    print(wordlist)

<|/ file filename=word