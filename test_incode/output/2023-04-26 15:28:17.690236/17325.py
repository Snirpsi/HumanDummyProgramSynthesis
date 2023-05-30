#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or opens a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        else:
            word = word.lower()
            if word not in wordlist:
                wordlist.append(word)
            else:
                print("That word is already in the list")
                
