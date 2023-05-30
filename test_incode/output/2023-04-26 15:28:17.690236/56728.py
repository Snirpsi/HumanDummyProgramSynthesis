#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and enumerates a list of numbers. """    
    words = ['cat', 'dog', 'mouse', 'elephant']
    numbers = [1, 2, 3, 4, 5]
    
    while True:
        print(' '.join(words))
        print(' '.join(str(number) for number in numbers))
        
        choice = input('\nEnter a number or type "quit" to quit.\n')
        
        if choice == 'quit':
            break
        
        number = int(choice)
        
        if number in numbers:
            print('Number found')
        else:
            print('Number not found')
        
        words.append(choice)
        numbers.append(number)
        
    print('\nThe end')
    
