#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or converts numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number > 0:
                numbers.append(number)
            else:
                numbers.append(number