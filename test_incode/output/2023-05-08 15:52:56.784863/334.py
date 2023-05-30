#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that converts numbers.
    while True:
        numbers.append(int(input("Enter a number: ")))
        #A break that stops the loop.
        if numbers[-1] == numbers[-2]:
            break
    print(numbers)

