#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers or calculates user input. """    
    
    # Get the user input
    number = int(input("Enter a number: "))
    
    # Calculate user input
    answer = number + 10
    
    # Print the result
    print("The answer is {}.".format(answer))
    
    # Return the result
    return answer
    
# Run the function
answer = calc_user_