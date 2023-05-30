#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    while True:
        numbers = [int(i) for i in input('Enter numbers: ').split()]
        
        numbers.append(numbers[-1] + numbers[-2])
        numbers.append(numbers[-1] + numbers[-2])
        
        print(' '.join(map(str, numbers)))
        
        if numbers[-1] == numbers[-2] and numbers[-1] != 0:
            break
        
    print('Done')

<|/ file filename=