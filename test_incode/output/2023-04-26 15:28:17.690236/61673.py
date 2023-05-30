#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        numbers = list(map(int, input().split()))
        numbers.sort()
        print(numbers)
        
        if numbers == []:
            break
            
        numbers.remove(numbers[0])
        print(numbers)
        
