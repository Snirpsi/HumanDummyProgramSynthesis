#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or adds a list of words. """    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    words = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    while True:
        print('\n'.join(fruits))
        print('\n'.join(words))
        
        choice = input('\nEnter your choice: ')
        
        if choice == 'quit':
            print('Goodbye!')
            break
        else:
            choice = choice.lower()
            
            if choice == 'add':
                fruits.append(input('Enter a fruit: ')) 
                words.append(input('Enter a word: ')) 
                
            elif choice == 'quit':
                print('Goodbye!')
                break
            else:
                print('Invalid choice!')
                
    print('\n'.join(fruits))
    print('\n'.join(words))
    
