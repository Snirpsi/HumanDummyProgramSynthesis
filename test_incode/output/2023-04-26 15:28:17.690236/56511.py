#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or removes a list of numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number in numbers:
                numbers.remove(number)
            else:
                print("Number not found.")
        except ValueError:
            print("Invalid number.")
        else:
            break
    print("Done.")
    
