#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and iterates over numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python convert_numbers.py <input_file>")
        sys.exit()
    
    input_file = sys.argv[1]
    
    with open(input_file) as input_file:
        for line in input_file:
            line = line.strip()
            
            if line:
                number = int(line)
                
                if number > 0:
                    number = number - 1
                    
                    print(number)
                    
                else:
                    print("Invalid number")
                    
            else:
                print("Invalid line")
                
