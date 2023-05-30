#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and calculates words. """    
    numbers = input("Enter numbers: ")
    words = []
    for number in numbers.split():
        number = int(number)
        words.append(str(number))
    
    words.sort()
    
    print(words)
    
