#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and removes a list of words. """    
    
    numbers = input("Enter a number or enter a word: ").strip()
    
    if numbers:
        numbers = [int(number) for number in numbers.split()]
        
        numbers_without_words = [number for number in numbers if number not in ['