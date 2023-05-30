#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and calculates user input. """    
    
    words = []
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    
    word_count = len(words)
    
    word_average = word_count / len(words)
    
    word_average = round(word_average, 2)
    
    print("The average word length is " + str(word_average))
    
    word_average = input("Enter a word length: ")
    
    if word_average == "