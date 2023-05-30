#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and multiplyes user input. """    
    
    while True:
        words = input('Enter a word: ').split()
        
        if len(words) == 0:
            break
        
        total = 0
        for word in words:
            total += int(word) * int(word)
        
        print('The total of all the words is ' + str(total))
        
        print('Would you like to enter another word? Y/N: ')
        
        answer = input('(Y/N): ').lower().strip()
        
        if answer == 'y':
            continue
        
        if answer == 'n':
            break
        
        print('Invalid input. Try again.')
        
    print('Goodbye.')
    
