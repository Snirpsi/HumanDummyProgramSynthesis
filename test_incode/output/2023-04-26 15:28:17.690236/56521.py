#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and stores a list of numbers. """    
    
    words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen'
    ]
    
    numbers = []
    
    for word in words:
        number = int(word)
        numbers.append(number)
    
    print(numbers)
    
