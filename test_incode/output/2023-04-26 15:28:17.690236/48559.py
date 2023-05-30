#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or opens fruits. """    
    
    # Get the user input or open fruits
    fruits = input("Please input the fruits: ")
    
    # Convert user input into fruit list
    fruits = fruits.split()
    
    # Convert fruit list into fruit dictionary
    fruits_dict = dict()
    for fruit in fruits:
        fruits_dict[fruit] = True
    
    # Print the fruit dictionary
    print(fruits_dict)
    
    # Print the fruit list
    print(fruits)
    
    # Print the fruit count
    print("The fruit count is", len(fruits))
    
    # Print the fruit list count
    print("The fruit list count is", len(fruits))
    
    # Print the fruit list with True values
    print("The fruit list with True values are", fruits_dict.keys())
    
    # Print the fruit list with True values and False values
    print("The fruit list with True values and False values are", fruits_dict.values())
    
    # Print the fruit list with True values and False values and True values
    print("The fruit list with True values and False values and True values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values
    print("The fruit list with True values and False values and True values and False values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values and True values
    print("The fruit list with True values and False values and True values and False values and True values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values and True values and False values
    print("The fruit list with True values and False values and True values and False values and True values and False values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values and True values and False values and True values
    print("The fruit list with True values and False values and True values and False values and True values and False values and True values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values and True values and False values and True values and False values
    print("The fruit list with True values and False values and True values and False values and True values and False values and True values and False values are", fruits_dict.items())
    
    # Print the fruit list with True values and False values and True values and False values and True values and False values and True values and False values and True values
    print("The fruit list with True values and False values and True 