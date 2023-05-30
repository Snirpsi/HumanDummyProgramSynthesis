#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and iterates over fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = ''
        
        while True:
            fruit = input('Enter a fruit: ')
            if fruit == '':
                break
            
            if fruit in fruits:
                print('{} is a fruit!'.format(fruit))
                break
            else:
                print('{} is not a fruit!'.format(fruit))
        
        print('{} is your favorite fruit!'.format(fruit))
        
        print('Would you like to play again? Y/N')
        playAgain = input('Y/N: ')
        if playAgain == 'Y':
            break
        else:
            print('Bye!')
            
    print('Bye!')
    
