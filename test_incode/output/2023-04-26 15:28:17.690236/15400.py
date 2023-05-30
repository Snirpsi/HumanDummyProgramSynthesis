#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or adds user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python open.py <numbers>")
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            sys.exit()
        
        if number < 0:
            print("Negative number")
            sys.exit()
        
        if number == 0:
            print("Zero")
            sys.exit()
        
        if number == 1:
            print("One")
            sys.exit()
        
        if number == 2:
            print("Two")
            sys.exit()
        
        if number == 3:
            print("Three")
            sys.exit()
        
        if number == 4:
            print("Four")
            sys.exit()
        
        if number == 5:
            print("Five")
            sys.exit()
        
        if number == 6:
            print("Six")
            sys.exit()
        
        if number == 7:
            print("Seven")
            sys.exit()
        
        if number == 8:
            print("Eight")
            sys.exit()
        
        if number == 9:
            print("Nine")
            sys.exit()
        
        if number == 10:
            print("Ten")
            sys.exit()
        
        if number == 11:
            print("Eleven")
            sys.exit()
        
        if number == 12:
            print("Twelve")
            sys.exit()
        
        if number == 13:
            print("Thirteen")
            sys.exit()
        
        if number == 14:
            print("Fourteen")
            sys.exit()
        
        if number == 15:
            print("Fifteen")
            sys.exit()
        
        if number == 16:
            print("Sixteen")
            sys.exit()
        
        if number == 17:
            print("Seventeen")
            sys.exit()
        
        if number == 18:
            print("Eighteen")
            sys.exit()
        
        if number == 19:
            print("Nineteen")
            sys.exit()
        
        if number == 20:
            print("Twenty")
            sys.exit()
        
        if number == 21:
            print("Twenty-one")
            sys.exit()
        
        if number == 22:
            print("Twenty-two")
            sys.exit()
        
        if number == 23:
            print("Twenty-three")
            sys.exit()
        
        if number == 24:
            print("Twenty-four")
            sys.exit()
        
        if number == 25:
            print("Twenty-five")
            sys.exit()
        
        if number == 26:
            print("Twenty-six")
            sys.exit()
        
        if number == 27:
            print("Twenty-seven")
            sys.exit()
        
