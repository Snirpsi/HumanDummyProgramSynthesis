#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers and opens a port. """    
    port = '/dev/ttyUSB0'
    numbers = []
    
    # Open the port and store a list of numbers in it.
    portOpen = serial.Serial(port, 9600, timeout=1)
    
    # Store the list of numbers in it.
    numbers.append(portOpen.readline())
    
    # Close the port.
    portOpen.close()
    
    # Print the list of numbers in it.
    print(numbers)
    
    # Print the list of numbers in it.
    print(numbers[0])
    
    # Print the list of numbers in it.
    print(numbers[2])
    
    # Print the list of numbers in it.
    print(numbers[3])
    
    # Print the list of numbers in it.
    print(numbers[4])
    
    # Print the list of numbers in it.
    print(numbers[5])
    
    # Print the list of numbers in it.
    print(numbers[6])
    
    # Print the list of numbers in it.
    print(numbers[7])
    
    # Print the list of numbers in it.
    print(numbers[8])
    
    # Print the list of numbers in it.
    print(numbers[9])
    
    # Print the list of numbers in it.
    print(numbers[10])
    
    # Print the list of numbers in it.
    print(numbers[11])
    
    # Print the list of numbers in it.
    print(numbers[12])
    
    # Print the list of numbers in it.
    print(numbers[13])
    
    # Print the list of numbers in it.
    print(numbers[14])
    
    # Print the list of numbers in it.
    print(numbers[15])
    
    # Print the list of numbers in it.
    print(numbers[16])
    
    # Print the list of numbers in it.
    print(numbers[17])
    
    # Print the list of numbers in it.
    print(numbers[18])
    
    # Print the list of numbers in it.
    print(numbers[19])
    
    # Print the list of numbers in it.
    print(numbers[20])
    
    # Print the list of numbers in it.
    print(numbers[21])
    
    # Print the list of numbers in it.
    print(numbers[22])
    
    # Print the list of numbers in it.
    print(numbers[23])
    
    # Print the list of numbers in it.
    print(numbers[24])
    
    # Print the list of numbers in it.
    print(numbers[25])
    
    # Print the list of numbers in it.
    print(numbers[26])
    
    # Print the list of numbers in it.
    print(numbers[27])
    
    # 