#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that iterates over numbers.
    #It prints them out in reverse order.
    for number in numbers:
        print(number)
        numbers.append(number*2)
    print(numbers)

