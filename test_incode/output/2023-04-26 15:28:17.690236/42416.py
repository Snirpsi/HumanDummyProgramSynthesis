#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or adds a list of words. """    
    while True:
        choice = input("Choose a number or word: ").lower()
        if choice == 'quit':
            break
        elif choice == '1':
            numbers = [int(x) for x in input("Enter a number: ").split()]
            print(numbers)
        elif choice == '2':
            words = [x.capitalize() for x in input("Enter a word: ").split()]
            print(words)
        else:
            print("Invalid input. Try again.")
