#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or enumerates a list of words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        
        choice = input('Choose an option: ')
        
        if choice == 'exit':
            break
        
        elif choice == '1':
            
            print('The first three letters of the word are: ', words[:3])
            
        elif choice == '2':
            
            print('The last three letters of the word are: ', words[-3:])
            
        elif choice == '3':
            
            print('The first five letters of the word are: ', words[:5])
            
        elif choice == '4':
            
            print('The last five letters of the word are: ', words[-5:])
            
        elif choice == '5':
            
            print('The first ten letters of the word are: ', words[:10])
            
        elif choice == '6':
            
            print('The last ten letters of the word are: ', words[-10:])
            
        elif choice == '7':
            
            print('The first eleven letters of the word are: ', words[:20])
            
        elif choice == '8':
            
            print('The last eleven letters of the word are: ', words[-20:])
            
        elif choice == '9':
            
            print('The first twenty letters of the word are: ', words[:21])
            
        elif choice == '10':
            
            print('The last twenty letters of the word are: ', words[-21:])
            
        elif choice == '11':
            
            print('The first thirty letters of the word are: ', words[:30])
            
        elif choice == '12':
            
            print('The last thirty letters of the word are: ', words[-30:])
            
        elif choice == '13':
            
            print('The first fourty letters of the word are: ', words[:40])
            
        elif choice == '14':
            
            print('The last fourty letters of the word are: ', words[-40:])
            
        elif choice == '15':
            
            print('The first fifty letters of the word are: ', words[:50])
            
        elif choice == '16':
            
            print('The last fifty letters of the word are: ', words[-50:])
            
        elif choice == '17':
            
            print('The first sixty letters of the word are: ', words[:60])
            
        elif choice == '18':
            
            print('The last sixty letters of the word are: ', 