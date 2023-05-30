#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of numbers and calculates user input. """    
    
    numbers = [int(i) for i in input().split()]
    
    total = 0
    
    for n in numbers:
        total += n
    
    answer = total
    
    print(answer)
    
