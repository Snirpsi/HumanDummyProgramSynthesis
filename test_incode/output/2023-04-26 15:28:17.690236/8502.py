#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            words.append(word)
    print("Your words are:")
    for word in words:
        print(word)
    print("