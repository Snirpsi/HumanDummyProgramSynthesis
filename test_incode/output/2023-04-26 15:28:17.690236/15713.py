#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and calculates words. """    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        if number < 0:
            print("Negative numbers are not allowed")
        elif number > 10:
            print("Numbers greater than 10 are not allowed")
        elif number % 2 == 0:
            print("Even numbers are not allowed")
        else:
            word = number % 2
            print(word)
            number = number // 2
            print(number)
            
