#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    while True:
        numbers = [int(i) for i in input().split()]
        numbers.extend(range(numbers[0], numbers[-1] + 1))
        
        # Print the list of numbers
        print(' '.join(map(str, numbers)))
        
        # Calculate and print the sum of the numbers
        total = sum(numbers)
        print('The sum is', total)
        
        # Print the remainder
        total = int(total) % 10
        print('The remainder is', total)
        
        # Print the quotient
        total = int(total) // 10
        print('The quotient is', total)
        
        # Print the remainder and quotient
        total = int(total) % 10
        print('The remainder and quotient is', total)
        
        # Print the remainder and quotient and so on
        total = int(total) % 10
        print('The remainder and quotient and so on is', total)
        
        # Print the remainder and quotient and so on
        total = int(total) % 10
        print('The remainder and quotient and so on and so on is', total)
        
        # Print the remainder and quotient and so on
        total = int(total) % 10
        print('The remainder and quotient and so on and so on and so on is', total)
        
        # Print the remainder and quotient and so on
        total = int(total) % 10
        print('The remainder and quotient and so on and so on and so on and so on is', total)
        
        # Print the remainder and quotient and so on
        total = int(total) % 10
        print('The remainder and quotient and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so on and so 