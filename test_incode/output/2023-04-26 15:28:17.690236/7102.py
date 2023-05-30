#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or calculates user input. """    
    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple!")
        elif fruit == "orange":
            print("You chose orange!")
        elif fruit == "banana":
            print("You chose banana!")
        else:
            print("You chose something else!")
            
        print("Do you want to continue? Y/N: ")
        
        if input("Do you want to continue? Y/N: ") == "Y":
            break
        
    print("Thank you for using my program!")
    
