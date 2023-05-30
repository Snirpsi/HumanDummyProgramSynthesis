#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that requests numbers.
    #It prints them out one by one.
    #The function will run until it gets an error.
    #The error will be printed out to the console.
    numbers_requester = requester(numbers)
    try:
        numbers_requester()
    except Exception as error:
        print(error)

