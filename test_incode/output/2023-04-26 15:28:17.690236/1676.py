#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and multiplyes a list of words. """    
    numbers = [int(x) for x in input().split()]
    words = [x.strip() for x in input().split()]
    
    numbers_multiplied = []
    for number in numbers:
        numbers_multiplied.append(number * words[number])
    
    print(" ".join(map(str, numbers_multiplied)))
