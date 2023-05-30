#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers and enumerates words. """    
    numbers = input("Enter a list of numbers: ")
    words = []
    for number in numbers.split(","):
        words.append(number)
    print("The words are:")
    for word in words:
        print(word)
    
