#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and stores numbers. """    
    words = []
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number > len(words):
            words.append(number)
        else:
            numbers.append(number)
        
        print('The numbers are: ', numbers)
        print('The words were: ', words)
        print('The total is: ', sum(numbers), ' ', sum(words))
        
        print('Would you like to enter another number? ')
        
        choice = input('Y/N: ')
        if choice == 'Y' or choice == 'y':
            continue
        elif choice == 'N' or choice == 'n':
            break
        else:
            print('Invalid input.')
            
    print('Goodbye!')
    
