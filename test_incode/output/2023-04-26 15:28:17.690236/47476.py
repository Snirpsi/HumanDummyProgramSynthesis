#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and opens a list of numbers. """    
    
    words = input("Enter the words: ")
    numbers = input("Enter the numbers: ")
    
    words = words.split()
    numbers = numbers.split()
    
    removed = []
    
    for word in words:
        if word in numbers:
            removed.append(word)
    
    for number in numbers:
        if number not in removed:
            removed.append(number)
    
    numbers = removed
    
    numbers = " ".join(numbers)
    
    print(numbers)
    
