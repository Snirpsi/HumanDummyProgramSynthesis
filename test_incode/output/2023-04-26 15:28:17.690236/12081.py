#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        try:
            user = input("Enter a number: ")
            
            if user.isdigit():
                number = int(user)
                
                if number > 0:
                    number = number - 1
                    
                    while number > 0:
                        print(number)
                        number = number - 1
                        
                else:
                    number = number + 1
                    
                    while number < 10:
                        print(number)
                        number = number + 1
                        
            else:
                print("Invalid input.")
                
        except ValueError:
            print("Invalid input.")
            
