#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    def enumerate(numbers):
        it = iter(numbers)
        count = 0
        while count < len(numbers):
            yield count, it.next()
            count += 1

