#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or removes a list of words. """    
    
    while(True):
        
        command = input('> ')
        
        if command == 'quit':
            break
        
        elif command == 'remove':
            
            number = input('> ')
            
            if number == 'quit':
                break
            
            number = int(number)
            
            if number > 0:
                
                number = number - 1
                
                number = str(number)
                
                print('> ' + str(number))
                
            else:
                print('> quit')
                
        elif command == 'removeall':
            
            wordlist = input('> ')
            
            if wordlist == 'quit':
                break
            
            wordlist = wordlist.split(' ')
            
            wordlist = [word.strip() for word in wordlist]
            
            wordlist = [word for word in wordlist if word]
            
            print('> ' + ' '.join(wordlist))
            
        else:
            print('> invalid command')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
