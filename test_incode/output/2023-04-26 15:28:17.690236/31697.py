#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and returns user input. """    
    
    # Create a list to store the numbers and then store user input into it.
    numbers = []
    
    # Create a loop that will ask user for input. 
    while True:
        # Ask user for input from the user. 
        number = int(input("Enter a number: "))
        
        # Append the number to the list.
        numbers.append(number)
        
        # Ask user if they want to continue or quit.
        answer = input("Do you want to continue (y/n)? ")
        
        # If the user enters y then quit the loop.
        if answer == "y":
            break
        
        # If the user enters n then exit the loop.
        elif answer == "n":
            break
        
        # If the user enters anything else then ask for user input.
        else:
            print("Invalid input. Please try again.")
    
    # Return the list.
    return numbers
    
# Run the program and store user input into numbers.
numbers = main()
    
# Print the numbers to the user.
print("The numbers are: ", *numbers)
    
# Print the total of the numbers.
print("The total of the numbers is ", sum(numbers))
</cell>
<text>
Now that you have learned about lists, we will be using them in our programs. In this lesson we will learn about dictionaries and other data structures. We will also learn about functions. We will also learn about loops.


</text>
<text>
Dictionaries
Dictionaries are a type of data structure that allows you to store key-value pairs. A dictionary is a collection of key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that allows you to store key-value pairs. A dictionary is a type of data structure that 