#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or converts fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'cherry']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        if word in fruits:
            print(word)
        else:
            fruits.append(word)
            
    print('The fruits:', fruits)
    
