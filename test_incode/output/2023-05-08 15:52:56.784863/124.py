#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that stores a list of numbers.
    def storeList(numbers):
        #Store the list in a new list.
        newList = [1,2,3,4,9]
        #Iterate through the list and add each number to the new list.
        for number in numbers:
            newList.append(number)
        #Return the new list.
        return newList
    #Call the function with the list as an argument.
    print(storeList(numbers))

