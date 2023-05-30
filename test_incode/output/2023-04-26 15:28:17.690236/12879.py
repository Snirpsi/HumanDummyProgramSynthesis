#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or stores numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # iterate over user input
        for num in sys.argv[1:]:
            print(num)
            
    else:
        
        # store numbers in file
        numbers = open('numbers.txt', 'w')
        
        # iterate over user input
        for num in range(1, 11):
            
            # write number to file
            numbers.write(str(num) + '\n')
            
            # increment number
            num += 1
            
        # close file
        numbers.close()
        
        # print number of numbers
        print('Number of numbers: ' + str(number