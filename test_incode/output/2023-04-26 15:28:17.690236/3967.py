#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of numbers and opens words. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    words = []
    for number in numbers:
        words.append(str(number))
    
    words.sort()
    
    print("\n".join(words))
    
