#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py numbers.txt")
        sys.exit()
    
    numbers = open(sys.argv[1], 'r')
    
    numbers_str = ''
    
    for line in numbers:
        numbers_str += line
    
    numbers = numbers_str.split('\n')
    
    for number in numbers:
        number = number.strip()
        
        try:
            number = int(number)
        except ValueError:
            print("Error: invalid number: " + number)
            continue
        
        numbers.append(number)
    
    numbers.sort()
    
    print("\n".join(numbers))
    
    numbers.close()
    
