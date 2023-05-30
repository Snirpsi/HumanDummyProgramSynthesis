#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        print(numbers)
        
        numbers = [numbers[0]+numbers[1],numbers[2]+numbers[3],numbers[4]+numbers[5],numbers[6]+numbers[7],numbers[8]+numbers[9],numbers[10]+numbers[11]]
        
