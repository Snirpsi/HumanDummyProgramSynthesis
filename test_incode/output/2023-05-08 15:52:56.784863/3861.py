#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #It then prints out the numbers in that list.
    #It then asks the user if they want to quit.
    numbers_opener = opener(numbers)
    while True:
        number = numbers_opener.readline()
        if number == 'q':
            break
        print(number)
    numbers_opener.close()

