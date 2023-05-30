#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or calculates words. """    
    while True:
        try:
            word = input('Enter a word: ')
            
            if word == 'quit':
                break
            
            if word == 'add':
                word1 = input('Enter the first word: ')
                word2 = input('Enter the second word: ')
                
                word3 = input('Enter the third word: ')
                
                print('The word ' + word1 + ' was added to' + ' ' + word2 + ' and' + ' ' + word3 + '.')
                
            elif word == 'multiply':
                word1 = input('Enter the first word: ')
                word2 = input('Enter the second word: ')
                
                word3 = input('Enter the third word: ')
                
                print('The word ' + word1 + ' was multiplied by' + ' ' + word2 + ' and' + ' ' + word3 + '.')
                
            elif word == 'divide':
                word1 = input('Enter the first word: ')
                word2 = input('Enter the second word: ')
                
                word3 = input('Enter the third word: ')
                
                print('The word ' + word1 + ' was divided by' + ' ' + word2 + ' and' + ' ' + word3 + '.')
                
            else:
                print('Sorry, I do not recognize that word.')
                
        except KeyboardInterrupt:
            print('\nBye!')
            break
        
