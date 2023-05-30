#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and opens a list of numbers. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if len(words) == 3:
            print('You entered a total of ', len(words), ' words.')
            
            print('Here are your words: ')
            
            for word in words:
                print(word)
            
            print('')
            
            print('Here are the numbers: ')
            
            for number in words:
                print(number)
            
            print('')
            
            print('Goodbye!')
            
            break
            
        else:
            print('Too many words. Try again.')
            
    print('Goodbye!')
    
