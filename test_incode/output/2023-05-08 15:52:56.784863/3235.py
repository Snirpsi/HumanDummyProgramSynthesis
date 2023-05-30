#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its contents
    while True:
        numbers.append(int(input("Enter a number: ")))
        #A endless loop that prints numbers to stdout
        print(numbers)
        #A endless loop that closes numbers.txt and exits
        break

