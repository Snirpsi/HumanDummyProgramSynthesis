#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            print(number)
            #numbers.append(number)
            #print(numbers)
            #numbers.pop()

