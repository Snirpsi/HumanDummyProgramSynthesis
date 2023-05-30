#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and opens fruits. """    
    numbers = open('numbers.txt')
    fruits = open('fruits.txt')
    
    numbers_fruits = numbers.readlines()
    fruits_numbers = fruits.readlines()
    
    numbers_fruits = [int(number) for number in numbers_fruits]
    fruits_numbers = [int(fruit) for fruit in fruits_numbers]
    
    numbers_fruits.sort()
    fruits_numbers.sort()
    
    numbers_fruits = numbers_fruits[:5]
    fruits_numbers = fruits_numbers[:5]
    
    numbers_fruits_string = " ".join(str(number) for number in numbers_fruits)
    fruits_numbers_string = " ".join(str(fruit) for fruit in fruits_numbers)
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_string = fruits_numbers_string.replace(' ', '')
    
    numbers_fruits_string = numbers_fruits_string.strip()
    fruits_numbers_string = fruits_numbers_string.strip()
    
    numbers_fruits_string = numbers_fruits_string.split()
    fruits_numbers_string = fruits_numbers_string.split()
    
    numbers_fruits_string = " ".join(numbers_fruits_string)
    fruits_numbers_string = " ".join(fruits_numbers_string)
    
    numbers_fruits_string = numbers_fruits_string.replace(',', '')
    fruits_numbers_string = fruits_numbers_string.replace(',', '')
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_string = fruits_numbers_string.replace(' ', '')
    
    numbers_fruits_string = numbers_fruits_string.split()
    fruits_numbers_string = " ".join(fruits_numbers_string)
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_string = fruits_numbers_string.replace(' ', '')
    
    numbers_fruits_string = numbers_fruits_string.replace(',', '')
    fruits_numbers_string = fruits_numbers_string.replace(',', '')
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_string = fruits_numbers_string.replace(' ', '')
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_string = fruits_numbers_string.replace(' ', '')
    
    numbers_fruits_string = numbers_fruits_string.replace(' ', '')
    fruits_numbers_