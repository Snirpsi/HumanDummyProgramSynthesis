#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers and multiplyes words. """    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    numbers = numbers.split()
    words = words.split()
    numbers = map(int, numbers)
    words = map(int, words)
    numbers = sum(numbers)
    words = sum(words)
    numbers = numbers * words
    print("The sum of the numbers is ", numbers)
    print("The sum of the words is ", words)
    print("The product of the numbers is ", numbers * words)
