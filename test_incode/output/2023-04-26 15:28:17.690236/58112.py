#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 number_to_list.py <numbers>")
        exit(1)
    
    numbers = sys.argv[1:]
    
    numbers_as_string = ""
    for number in numbers:
        numbers_as_string += str(number)
    
    numbers_as_string = numbers_as_string.replace("[", "").replace("]", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_as_string.replace(",", "")
    numbers_as_string = numbers_as_string.replace("'", "")
    numbers_as_string = numbers_