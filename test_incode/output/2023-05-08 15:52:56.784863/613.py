#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that calculates numbers.
    while True:
        print(sum(numbers))
        numbers.append(numbers[-1]+1)
        #A break that stops the loop.

