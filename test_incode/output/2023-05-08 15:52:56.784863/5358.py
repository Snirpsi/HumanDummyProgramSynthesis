#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that calculates a list of numbers.
    while True:
        numbers.append(numbers[-1] + numbers[-2])
        print(numbers)
        numbers.pop()
        #A break that stops the loop
        if numbers == []:
            break
        #A break that stops the loop
        if numbers == []:
            break

