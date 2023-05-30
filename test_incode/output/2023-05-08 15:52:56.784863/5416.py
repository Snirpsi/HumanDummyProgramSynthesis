#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #The user can then choose to quit or continue to enter numbers.
    while True:
        choice = input("Enter a number or q to quit: ")
        if choice == 'q':
            break
        elif choice == '1':
            numbers.append(int(input("Enter a number: ")))
        elif choice == '2':
            numbers.append(int(input("Enter a number: ")))
        elif choice == '3':
            numbers.append(int(input("Enter a number: ")))
        elif choice == '4':
            numbers.append(int(input("Enter a number: ")))
        elif choice == '5':
            numbers.append(int(input("Enter a number: ")))
        elif choice == 'q':
            break
        else:
            print("Invalid input")

