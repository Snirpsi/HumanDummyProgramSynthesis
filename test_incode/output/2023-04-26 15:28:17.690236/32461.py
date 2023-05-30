#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers and calculates user input. """    
    
    while True:
        number = int(input('Enter a number: '))
        
        if number == -1:
            break
        
        print('The number you entered is {}'.format(number))
        
        answer = input('Do you want to add another number? (y/n): ')
        
        if answer == 'y':
            number = number + number
            print('The number you entered is {}'.format(number))
            
            answer = input('Do you want to subtract another number? (y/n): ')
            
            if answer == 'y':
                number = number - number
                print('The number you entered is {}'.format(number))
                
                answer = input('Do you want to multiply another number? (y/n): ')
                
                if answer == 'y':
                    number = number * number
                    print('The number you entered is {}'.format(number))
                    
                    answer = input('Do you want to divide another number? (y/n): ')
                    
                    if answer == 'y':
                        number = number / number
                        print('The number you entered is {}'.format(number))
                        
                        answer = input('Do you want to quit (y/n): ')
                        
                        if answer == 'y':
                            break
                        
                        else:
                            print('Invalid input.')
                            
                            continue
                    
                    else:
                        print('Invalid input.')
                        
                        continue
                    
                else:
                    print('Invalid input.')
                    
                    continue
                
            else:
                print('Invalid input.')
                
                continue
            
        else:
            print('Invalid input.')
            
            continue
    
    print('Thank you!')
    
