#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that adds numbers.
    #The program will exit when "q" is entered.
    while True:
        numbers.append(int(input("Enter a number: ")))
        if input("Do you want to add another number? y/n: ") == "y":
            numbers.append(int(input("Enter a number: ")))
        else:
            break
    print(numbers)

