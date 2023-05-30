#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and multiplyes numbers. """    
    words = input("Enter a sentence: ")
    numbers = input("Enter numbers: ")
    
    wordList = words.split()
    numberList = numbers.split()
    
    total = 0
    
    for word in wordList:
        total += int(word)
    
    for number in numberList:
        total += int(number)
    
    print(total)
    
