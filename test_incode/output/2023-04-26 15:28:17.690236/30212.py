#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens numbers. """    
    words = open("words.txt").read().splitlines()
    numbers = open("numbers.txt").read().splitlines()
    for word in words:
        numbers.append(word)
    for number in numbers:
        print(number, end="")
