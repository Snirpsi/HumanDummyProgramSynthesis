#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that converts a list of numbers.
    #It will print each number in turn.
    #The program will exit after printing one number.
    #The program will continue to loop until the user enters 0.
    while(True):
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            print(number)
            numbers.append(number)
    print(numbers)

