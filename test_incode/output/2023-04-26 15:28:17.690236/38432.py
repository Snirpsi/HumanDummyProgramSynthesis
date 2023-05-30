#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        numbers = [int(n) for n in f.read().strip().split(",")]
        
    with open(filename, "w") as f:
        f.write(",".join(map(str, numbers)))
        
    print("Removed {} numbers from {}".format(len(numbers), filename))
