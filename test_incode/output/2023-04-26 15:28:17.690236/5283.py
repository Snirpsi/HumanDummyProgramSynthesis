#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or stores user input. """    
    
    # Define the fruit list
    fruits = ['apple', 'banana', 'orange', 'pear']
    
    # Define the fruit dictionary
    fruitDict = {fruit: index for index, fruit in enumerate(fruits)}
    
    # Define the fruit counter
    fruitCounter = 0
    
    # Define the fruit input function
    def fruitInput():
        """ Gets user input for fruit name. """
        fruitName = input('Enter a fruit name: ')
        
        # Return the fruit name
        return fruitName
    
    # Define the fruit output function
    def fruitOutput():
        """ Gets user input for fruit index. """
        fruitIndex = input('Enter a fruit index: ')
        
        # Return the fruit index
        return fruitIndex
    
    # Define the fruit input loop
    while True:
        # Define the fruit input function
        fruitInput = fruitInput()
        
        # Print the fruit name
        print('The fruit name is ' + fruitInput)
        
        # Print the fruit index
        print('The fruit index is ' + fruitDict[fruitInput])
        
        # Print the fruit counter
        print('The fruit counter is ' + str(fruitCounter))
        
        # Print the fruit input again
        print('The fruit input again')
        
        # Print the fruit output again
        print('The fruit output again')
        
        # Define the fruit output function
        fruitOutput = fruitOutput()
        
        # Print the fruit name
        print('The fruit name is ' + fruitOutput)
        
        # Print the fruit index
        print('The fruit index is ' + fruitDict[fruitOutput])
        
        # Print the fruit counter
        print('The fruit counter is ' + str(fruitCounter))
        
        # Print the fruit input again
        print('The fruit input again')
        
        # Print the fruit output again
        print('The fruit output again')
        
        # Define the fruit input loop
