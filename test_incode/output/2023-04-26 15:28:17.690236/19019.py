#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    numbers = []
    for line in lines:
        numbers.append(int(line))
    
    numbers = list(set(numbers))
    
    numbers_filtered = numbers[:]
    
    for number in numbers_filtered:
        if number % 2 == 0:
            numbers_filtered.remove(number)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(numbers_filtered))
        
    print("Removed %d numbers" % len(numbers_filtered))
    
