#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and multiplyes user input. """    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == 'q':
            break
        words.append(word)
    
    total = 0
    for word in words:
        total += word
    
    print("The total is", total)
    
