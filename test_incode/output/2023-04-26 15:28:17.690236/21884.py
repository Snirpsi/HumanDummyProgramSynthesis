#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and multiplyes words. """    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    numbers = numbers.split()
    words = words.split()
    numbers = [int(n) for n in numbers]
    words = [w.lower() for w in words]
    numbers = map(int, numbers)
    words = map(