#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that removes numbers.
    def remove(numbers):
        numbers = [x for x in numbers if x not in numbers]
        return numbers
    numbers = remove(numbers)
    print(numbers)

