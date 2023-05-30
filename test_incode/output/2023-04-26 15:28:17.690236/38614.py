#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    # Read numbers from stdin
    numbers = map(int, sys.stdin.readline().split())
    
    # Calculate sum
    total = 0
    for number in numbers:
        total += number
    
    # Print result
    print(total)
    
    # Close stdin
    sys.stdin.close()
    
    # Close stdout
    sys.stdout.close()
    
    # Close stderr
    sys.stderr.close()
    
    # Close all files
    for file in [sys.stdin, sys.stdout, sys.stderr]:
        file.close()
    
    # Exit program
    sys.exit(0)

<|/ file filename=sum.py |>