#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or converts a port. """    
    while True:
        word = input("Enter a word: ")
        
        if word == 'exit':
            break
        
        if word == 'convert':
            convert_port()
        
        if word == 'add':
            add_word()
        
        if word == 'help':
            help_menu()
        
        if word == 'quit':
            break
        
        print("Invalid command")
        
    print("Goodbye")
