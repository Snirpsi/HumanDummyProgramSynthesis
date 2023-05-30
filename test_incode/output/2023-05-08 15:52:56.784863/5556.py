#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that opens a list of numbers.
    #The function then prints out the numbers in that list.
    #The function then prints out a message saying "Done."
    #The function then closes the list.
    numbers = openFile()
    print(numbers)
    print("Done.")
    numbers.close()

