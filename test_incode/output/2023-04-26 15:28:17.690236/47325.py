#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of numbers or adds numbers. """    
    
    # Get the input from the user
    numbers = input()
    
    # Convert the input to a list
    numbers = list(map(int, numbers.split(',')))
    
    # Print the result
    print(numbers)
    
    # Return the list
    return numbers
    
# Run the function
numbers = main()
print(numbers)
</cell>
<cell>

</cell>
<|/ file dstars=1 source=github ext=.ipynb:python |>