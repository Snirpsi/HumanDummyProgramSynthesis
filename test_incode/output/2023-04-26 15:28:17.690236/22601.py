#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts fruits or iterates over user input. """    
    
    fruit = input("Enter a fruit or iterate over it: ")
    
    if fruit == "fruit":
        print("Fruit converted")
    elif fruit == "iter":
        print("Iteration started")
        
        fruits = []
        
        while True:
            fruit = input("Enter a fruit or iterate over it: ")
            
            if fruit == "fruit":
                print("Fruit converted")
            elif fruit == "iter":
                print("Iteration started")
                
                fruits.append(fruit)
                
            else:
                print("Invalid input")
                
        print("Iteration ended")
        
    else:
        print("Invalid input")
        
    
