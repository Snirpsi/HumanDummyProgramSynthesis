#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #The function then prints the numbers in reverse order.
    #The function then closes the list.
    numbers = reverse_list(numbers)
    print(numbers)
    numbers.close()

