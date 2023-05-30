#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or opens a list of words. """    
    
    while True:
        
        list_to_remove = []
        
        try:
            list_to_remove = input("Enter a number or word: ")
            
        except EOFError:
            print("Goodbye!")
            break
        
        else:
            
            try:
                list_to_remove = list_to_remove.split()
                
            except AttributeError:
                print("You didn't enter a number.")
                
            else:
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()
                
                list_to_remove = list_to_remove.lower()
                
                list_to_remove = list_to_remove.split()
                
                list_to_remove = list_to_remove[0]
                
                list_to_remove = list_to_remove.strip()