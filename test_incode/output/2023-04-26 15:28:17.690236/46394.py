#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits or enumerates words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    fruits = ['orange', 'mango', 'cherry']
    
    while True:
        
        choice = input('Enter your choice: ')
        
        if choice == 'exit':
            break
        
        elif choice == 'fruit':
            
            print('You have selected a fruit.')
            
            for fruit in fruits:
                print('{} is awesome.'.format(fruit))
                
        elif choice == 'word':
            
            print('You have selected a word.')
            
            for word in words:
                print('{} is awesome.'.format(word))
                
        else:
            print('Invalid choice.')
            
    print('Goodbye!')
    
