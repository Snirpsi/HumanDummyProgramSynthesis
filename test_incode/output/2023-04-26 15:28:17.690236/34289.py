#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and multiplyes user input. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == "":
            break
    
    total = 0
    for word in words:
        total += word.count('a')
    
    print("The total is", total)
    
