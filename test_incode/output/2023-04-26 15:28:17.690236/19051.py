#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or opens a list of words. """    
    while True:
        words = []
        
        while True:
            word = input('Enter a word: ')
            if word == '':
                break
            words.append(word)
            
        print('\n'.join(words))
        
        if input('Do you want to add more words? (y/n): ').lower() == 'y':
            words = []
            
            for _ in range(int(input('How many words would you like to add? '))):
                word = input('Enter a word: ')
                if word == '':
                    break
                words.append(word)
            
            print('\n'.join(words))
            
        else:
            break
            
    print('Goodbye!')
    
