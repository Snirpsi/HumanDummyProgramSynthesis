#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers and prints user input. """    
    
    while True:
        
        number = input("Enter a number: ")
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            continue
        
        if number < 0:
            print("Negative number")
            continue
        
        if number == 0:
            print("Zero")
            continue
        
        if number > 10:
            print("Too big")
            continue
        
        if number < 10:
            print("Too small")
            continue
        
        print("Converting %s to integer" % number)
        
        number = int(number)
        
        print("Converted %s to integer" % number)
        
        number = float(number)
        
        print("Converted %s to float" % number)
        
        number = str(number)
        
        print("Converted %s to string" % number)
        
        number = str(number).upper()
        
        print("Converted %s to uppercase string" % number)
        
        number = str(number).lower()
        
        print("Converted %s to lowercase string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
        number = str(number).capitalize()
        
        print("Converted %s to capitalize string" % number)
        
        number = str(number).title()
        
        print("Converted %s to title string" % number)
        
