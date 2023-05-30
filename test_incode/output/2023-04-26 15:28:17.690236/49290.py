#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and calculates fruits. """    
    while True:
        fruits = input("Enter a number: ")
        try:
            fruits = int(fruits)
        except ValueError:
            print("Invalid input.")
        else:
            if fruits > 0:
                fruits_converted = fruits/10
                print("The fruits are converted:", fruits_converted)
            else:
                print("The fruits are converted: 0.")
