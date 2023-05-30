#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes fruits. """    
    
    words = input("Enter a word: ")
    
    if len(words) == 0:
        print("No words given.")
    else:
        words = words.split()
        
        fruits = input("Enter a fruit: ")
        
        if len(fruits) == 0:
            print("No fruits given.")
        else:
            fruits = fruits.split()
            
            remove = False
            
            for word in words:
                if word in fruits:
                    remove = True
            
            if remove == True:
                print("Removed fruits.")
            else:
                print("No fruits given.")
    
