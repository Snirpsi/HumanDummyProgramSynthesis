#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers or opens a list of words. """    
    
    while True:
        try:
            line = input('Enter a number: ')
            number = int(line)
            
            if number > 0 and number < 10:
                number = str(number)
                
                print(f'The number you entered is {number}')
                
            elif number > 10 or number < 0:
                print('Invalid number')
                
            else:
                print('Invalid input')
                
        except ValueError:
            print('Invalid input')
            
        except EOFError:
            print('End of file')
            
        except KeyboardInterrupt:
            print('Program terminated')
            
        else:
            print('Invalid input')
            
