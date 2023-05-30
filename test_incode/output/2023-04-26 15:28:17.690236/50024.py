#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or iterates over a list of numbers. """    
    
    words = ["cat", "dog", "mouse"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        print("\nWelcome to my little program!")
        print("\nWhat would you like to do?")
        print("\n1. Add a new word")
        print("\n2. Add a new number")
        print("\n3. Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            
            print("\nWhat would you like to add?")
            print("\n1. cat")
            print("\n2. dog")
            print("\n3. mouse")
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                
                print("\nYou just added a new word!")
                
                words.append(input("\nEnter your new word: "))
                
            elif choice == "2":
                
                print("\nYou just added a new number!")
                
                numbers.append(int(input("\nEnter your new number: ")))
                
            elif choice == "3":
                
                print("\nGoodbye!")
                
                break
                
            else:
                
                print("\nInvalid choice!")
                
        elif choice == "2":
            
            print("\nWhat would you like to add?")
            print("\n1. cat")
            print("\n2. dog")
            print("\n3. mouse")
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                
                print("\nYou just added a new word!")
                
                words.append(input("\nEnter your new word: "))
                
            elif choice == "2":
                
                print("\nYou just added a new number!")
                
                numbers.append(int(input("\nEnter your new number: ")))
                
            elif choice == "3":
                
                print("\nGoodbye!")
                
                break
                
            else:
                
                print("\nInvalid choice!")
                
        elif choice == "3":
            
            print("\nGoodbye!")
            
            break
            
        else:
            
            print("\nInvalid choice!")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    