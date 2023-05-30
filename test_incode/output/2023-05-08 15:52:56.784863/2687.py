#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    #The function returns two values: the first is the index of the first element
    #in the list, the second is the index of the last element in the list.
    #The function can be called as such:
    #enumerate([1,2,3,4,9])
    #The function returns the following values:
    #(0, 9), (2, 4), (3, 3), (4, 2), (5, 1)
    enumerated = enumerate(numbers)
    print(*enumerated)

