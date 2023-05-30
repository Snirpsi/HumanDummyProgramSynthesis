#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = list(map(int, numbers.split()))
    
    numbers.append(sum(numbers))
    
    print("The sum of the numbers is:", sum(numbers))
    
    print("The average of the numbers is:", sum(numbers) / len(numbers))
    
    print("The sum of the squares of the numbers is:", sum(map(lambda x: x**2, numbers)))
    
    print("The difference of the numbers is:", numbers[0] - numbers[1])
    
    print("The difference of the squares of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2)
    
    print("The difference of the differences of the numbers is:", numbers[0] - numbers[1] - numbers[2])
    
    print("The difference of the differences of the squares of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2 - numbers[2] ** 2)
    
    print("The difference of the differences of the differences of the numbers is:", numbers[0] - numbers[1] - numbers[2] - numbers[3])
    
    print("The difference of the differences of the differences of the differences of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2 - numbers[2] ** 2 - numbers[3] ** 2)
    
    print("The difference of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] - numbers[1] - numbers[2] - numbers[2] - numbers[3])
    
    print("The difference of the differences of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2 - numbers[2] ** 2 - numbers[3] ** 2 - numbers[4] ** 2)
    
    print("The difference of the differences of the differences of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] - numbers[1] - numbers[2] - numbers[2] - numbers[2] - numbers[3])
    
    print("The difference of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2 - numbers[2] ** 2 - numbers[3] ** 2 - numbers[4] ** 2 - numbers[5] ** 2)
    
    print("The difference of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] - numbers[1] - numbers[2] - numbers[2] - numbers[2] - numbers[2] - numbers[3])
    
    print("The difference of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the differences of the numbers is:", numbers[0] ** 2 - numbers[1] ** 2 - numbers[2] ** 2 - numbers[3] ** 2 - numbers[4] ** 2 - numbers[5] ** 2 - numbers[6] ** 2)
    
    print("The difference of the differences of the differences of the differences of the 