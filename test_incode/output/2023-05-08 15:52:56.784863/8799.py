#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that stores numbers.
    while True:
        numbers.append(input("Enter a number: "))
        if numbers[-1] == 'done':
            break
    print(numbers)

