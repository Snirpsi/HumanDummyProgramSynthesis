#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and multiplyes a port. """    
    port = int(input("Enter a port number: "))
    
    while True:
        
        choice = input("Do you want to add another port? (y/n)")
        
        if choice == "y":
            
            port *= 10
            
        elif choice == "n":
            
            break
        
        else:
            
            print("Invalid input. Try again.")
            
    
    print("The port number is:", port)
    
