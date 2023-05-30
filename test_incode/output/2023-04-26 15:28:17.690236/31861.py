#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and removes user input. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input("Enter a number: "))
            numbers.append(number)
        except ValueError:
            print("Invalid number")
            continue
        else:
            break
    
    numbers = list(set(numbers))
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    
    print("Numbers removed:", numbers_removed)
    
    numbers_added = numbers + [numbers_removed]
    
    print("Numbers added:", numbers_added)
    
    numbers_removed = numbers.pop()
    