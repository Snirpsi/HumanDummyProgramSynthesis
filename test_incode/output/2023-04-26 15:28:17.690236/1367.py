#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        choice = sys.argv[1]
        
        if choice == '1':
            
            numbers = range(1,10)
            
        elif choice == '2':
            
            numbers = range(1,11)
            
        elif choice == '3':
            
            numbers = range(1,12)
            
        elif choice == '4':
            
            numbers = range(1,13)
            
        elif choice == '5':
            
            numbers = range(1,14)
            
        elif choice == '6':
            
            numbers = range(1,15)
            
        elif choice == '7':
            
            numbers = range(1,16)
            
        elif choice == '8':
            
            numbers = range(1,17)
            
        elif choice == '9':
            
            numbers = range(1,18)
            
        else:
            
            print("Invalid choice")
            
    else:
        
        print("Usage: python webserver.py <choice>")
        
