#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    
    numbers = []
    
    for _ in range(int(input())):
        numbers.append(int(input()))
    
    numbers.sort()
    
    for number in numbers:
        print(number)
    
