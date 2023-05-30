#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and stores a list of numbers. """    
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
        
        numbers.append(int(line))
    
    words.sort()
    numbers.sort()
    
    print(" ".join(words))
    print(" ".join(str(number) for number in numbers))
    
    

<|/ file source=github |>