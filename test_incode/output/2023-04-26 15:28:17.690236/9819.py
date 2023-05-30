#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) == 1:
        words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    else:
        words = sys.argv[1:]
    
    words = [word.lower() for word in words]
    
    numbers = [int(word) for word in words]
    
    numbers = numbers + [0 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [1 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [2 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [3 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [4 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [5 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [6 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [7 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [8 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [9 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [10 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [11 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [12 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [13 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [14 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [15 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [16 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [17 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [18 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [19 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [20 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [21 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [22 for _ in range(len(numbers)-1)]
    
    numbers = numbers + [2