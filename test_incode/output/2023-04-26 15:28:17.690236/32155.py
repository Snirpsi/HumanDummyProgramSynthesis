#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers. """    
    numbers = [int(n) for n in input().split()]
    
    # Open the output file
    with open("output.txt", "w") as f:
        # Write the numbers to the output file
        f.write("\n".join(map(str, numbers)))
    
    # Close the output file
    f.close()

<|/ file filename=