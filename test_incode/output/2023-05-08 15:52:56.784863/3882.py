#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that prints a list of numbers.
    #The program will exit when 'q' is entered.
    while True:
        print(numbers)
        choice = input("Enter q to quit or any other key to continue: ")
        if choice == 'q':
            break
        else:
            numbers.append(int(choice))
    print(numbers)

