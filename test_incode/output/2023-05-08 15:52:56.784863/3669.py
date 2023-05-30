#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    #The function takes a list of numbers and returns 
    #the indices of the numbers in the list that 
    #are multiples of 3.
    def multiples_of_3(numbers):
        multiples = []
        for number in numbers:
            if number % 3 == 0:
                multiples.append(number)
        return multiples
    
    #The main function takes a list of numbers and 
    #prints the indices of the numbers in the list that 
    #are multiples of 3.
    multiples_of_3(numbers)
    

