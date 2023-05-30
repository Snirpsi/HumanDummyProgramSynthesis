#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        print('You have {} apples and {} bananas'.format(*fruits))
        
        print('Do you want to add more fruits?')
        
        answer = input('(y/n): ')
        
        if answer == 'y':
            fruits.append('orange')
            
            print('You have {} apples and {} bananas'.format(*fruits))
            
            print('Do you want to add more fruits?')
            
            answer = input('(y/n): ')
            
            if answer == 'y':
                fruits.append('kiwi')
                
                print('You have {} apples and {} bananas'.format(*fruits))
                
                print('Do you want to add more fruits?')
                
                answer = input('(y/n): ')
                
                if answer == 'y':
                    fruits.append('strawberry')
                    
                    print('You have {} apples and {} bananas'.format(*fruits))
                    
                    print('Do you want to add more fruits?')
                    
                    answer = input('(y/n): ')
                    
                    if answer == 'y':
                        fruits.append('watermelon')
                        
                        print('You have {} apples and {} bananas'.format(*fruits))
                        
                        print('Do you want to add more fruits?')
                        
                        answer = input('(y/n): ')
                        
                        if answer == 'y':
                            print('Thanks for playing!')
                            
                            break
                        
                        else:
                            print('Sorry, I did not understand your input.')
                            
                            continue
                        
                    else:
                        print('Sorry, I did not understand your input.')
                        
                        continue
                    
                else:
                    print('Sorry, I did not understand your input.')
                    
                    continue
                
            else:
                print('Sorry, I did not understand your input.')
                
                continue
            
        else:
            print('Thanks for playing!')
            
            break
        
    print('Thanks for playing!')
    
