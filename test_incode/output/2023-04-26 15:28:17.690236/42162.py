#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while(True):
        
        numbers.pop()
        
        if(len(numbers) == 0):
            break
        
        print("Numbers left: ", len(numbers))
        
        print("Numbers: ", numbers)
        
        print("Press enter to exit.")
        
        input()
        
    print("Done!")
    
