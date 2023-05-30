#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or adds a list of words. """    
    while True:
        choice = input("\nDo you want to add or remove numbers? (y/n): ")
        if choice == 'y':
            numbers = input("\nEnter numbers: ")
            numbers = [int(n) for n in numbers.split()]
            numbers.sort()
            print(numbers)
        elif choice == 'n':
            break
        else:
            print("Invalid input. Try again.")
