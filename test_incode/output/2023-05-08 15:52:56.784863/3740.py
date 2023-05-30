#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that removes a list of numbers.
    def remove(numbers):
        return numbers.remove(2)
    print(remove(numbers))

