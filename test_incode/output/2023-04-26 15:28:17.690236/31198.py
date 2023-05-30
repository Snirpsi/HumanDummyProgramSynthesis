#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        if number < 0:
            print("Negative numbers are not allowed. Try again.")
            continue
        if number == 0:
            print("You entered a zero. Try again.")
            continue
        if number == -1:
            print("You entered a negative number. Try again.")
            continue
        if number > 10:
            print("You entered a number greater than 10. Try again.")
            continue
        if number < 10:
            print("You entered a number less than 10. Try again.")
            continue
        if number % 2 == 0:
            print("You entered a number that is a perfect square. Try again.")
            continue
        if number % 3 == 0:
            print("You entered a number that is a perfect cube. Try again.")
            continue
        if number % 5 == 0:
            print("You entered a number that is a perfect five. Try again.")
            continue
        if number % 7 == 0:
            print("You entered a number that is a perfect seven. Try again.")
            continue
        if number % 9 == 0:
            print("You entered a number that is a perfect nine. Try again.")
            continue
        if number % 11 == 0:
            print("You entered a number that is a perfect ten. Try again.")
            continue
        if number % 13 == 0:
            print("You entered a number that is a perfect eleven. Try again.")
            continue
        if number % 15 == 0:
            print("You entered a number that is a perfect twelve. Try again.")
            continue
        if number % 17 == 0:
            print("You entered a number that is a perfect thirteen. Try again.")
            continue
        if number % 19 == 0:
            print("You entered a number that is a perfect fourteen. Try again.")
            continue
        if number % 23 == 0:
            print("You entered a number that is a perfect fifteen. Try again.")
            continue
        if number % 29 == 0:
            print("You entered a number that is a perfect sixteen. Try again.")
            continue
        if number % 31 == 0:
            print("You entered a number that is a perfect seventeen. Try again.")
            continue
        if number % 37 == 0:
            print("You entered a number that is a perfect eighteen. Try again.")
            continue
        if number % 43 == 0:
            print("You entered a number that is a perfect nineteen. Try again.")
            continue
        if number % 49 == 0:
            print("You entered a number that is a perfect twenty. Try again.")
            continue
        if number % 57 == 0:
            print("You entered 