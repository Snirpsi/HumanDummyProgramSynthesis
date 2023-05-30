#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or iterates over user input. """    
    
    fruitsToRemove = input("Enter fruits to remove: ")
    
    if fruitsToRemove == '':
        print("No fruits were removed")
    else:
        fruitsToRemove = fruitsToRemove.split()
        
        for fruit in fruitsToRemove:
            if fruit == 'apple':
                print("Apple")
            elif fruit == 'banana':
                print("Banana")
            elif fruit == 'cherry':
                print("Cherry")
            elif fruit == 'orange':
                print("Orange")
            elif fruit == 'peach':
                print("Peach")
            elif fruit == 'plum':
                print("Plum")
            elif fruit == 'raspberry':
                print("Raspberry")
            elif fruit == 'strawberry':
                print("Strawberry")
            elif fruit == 'watermelon':
                print("Watermelon")
            elif fruit == 'watermelon':
                print("Watermelon")
            else:
                print("Unknown fruit")
                
