#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or iterates over numbers. """    
    while True:
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print("{} is even".format(number))
            else:
                print("{} is odd".format(number))
        except ValueError:
            print("Invalid number")
        except KeyboardInterrupt:
            print("Exiting...")
            break
        
