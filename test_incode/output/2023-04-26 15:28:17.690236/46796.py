#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    print("The words are:")
    for word in words:
        print(word)
    print("