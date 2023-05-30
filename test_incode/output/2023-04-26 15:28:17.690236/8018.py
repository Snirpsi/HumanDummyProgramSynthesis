#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates numbers and opens words. """    
    
    # Read in input file
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    # Calculate numbers
    numbers = []
    for word in words:
        number = int(word)
        numbers.append(number)
    
    # Open files
    numbers_file = open(sys.argv[1], 'w')
    words_file = open(sys.argv[2], 'w')
    
    # Write numbers to file
    for number in numbers:
        numbers_file.write(str(number) + '\n')
    
    # Write words to file
    for word in words:
        words_file.write(word + '\n')
    
    # Close files
    numbers_file.close()
    words_file.close()
    
    # Close program
    exit()
