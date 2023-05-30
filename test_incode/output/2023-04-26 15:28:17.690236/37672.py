#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input and stores a list of numbers. """    
    
    # Define a function to multiply user input by a list of numbers
    def multiply(numbers, product):
        
        # Define a variable to store the product of user input by the numbers
        product = 0
        
        # Loop through each number in numbers and multiply it by the product
        for number in numbers:
            product *= number
        
        # Return the product of user input by the numbers
        return product
    
    # Define a function to store user input as a list of numbers
    def store_input():
        
        # Define a variable to store the user input
        numbers = []
        
        # Loop through each character in user input
        for character in input("Enter a number: "):
            
            # Append the character to the list of numbers
            numbers.append(character)
        
        # Return the list of numbers
        return numbers
    
    # Define a function to store user input as a list of numbers
    def store_numbers():
        
        # Define a variable to store the user input
        numbers = []
        
        # Loop through each character in user input
        for character in input("Enter a number: "):
            
            # Append the character to the list of numbers
            numbers.append(int(character))
        
        # Return the list of numbers
        return numbers
    
    # Define a function to store user input as a list of numbers
    def store_product():
        
        # Define a variable to store the user input
        numbers = []
        
        # Loop through each character in user input
        for character in input("Enter a number: "):
            
            # Append the character to the list of numbers
            numbers.append(int(character) * int(character))
        
        # Return the list of numbers
        return numbers
    
    # Define a function to store user input as a list of numbers
    def store_product_list():
        
        # Define a variable to store the user input
        numbers = []
        
        # Loop through each character in user input
        for character in input("Enter a number: "):
            
            # Append the character to the list of numbers
            numbers.append(int(character) * [int(character)])
        
        # Return the list of numbers
        return numbers
    
    # Define a function to store user input as a list of numbers
    def store_product_list_list():
        
        # Define a variable to store the user input
        numbers = []
        
        # Loop through each character in user input
        for character in input("Enter a number: "):
            
            # Append the character to the list of numbers
            numbers.append(int(character) * [int(character)])
        
        # Return the list of numbers
        return numbers
    
    # Define a function to store user input as a list of numbers
    def 