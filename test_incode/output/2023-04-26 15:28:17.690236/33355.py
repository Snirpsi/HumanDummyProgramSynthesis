#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or adds a list of numbers. """    
    
    wordlist = ["cat", "dog", "pig", "horse", "sheep", "cow", "zebra"]
    
    while True:
        
        choice = input("\nWhat would you like to do? ")
        
        if choice == "add":
            
            number = input("\nWhat number would you like to add? ")
            
            wordlist.append(number)
            
        elif choice == "remove":
            
            number = input("\nWhat number would you like to remove? ")
            
            wordlist.remove(number)
            
        else:
            
            print("\nSorry, I didn't understand that.")
            
