#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        numbers.append(numbers[-1] + numbers[-2])
        
        print("The last number is {}".format(numbers[-1]))
        print("The second last number is {}".format(numbers[-2]))
        
        print("The list of numbers is: {}".format(numbers))
        
        print("Press enter to exit.")
        
        input()
        
