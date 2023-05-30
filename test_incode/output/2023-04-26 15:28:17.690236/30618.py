#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Open the webpage and allow the user to enter their name
    webbrowser.open('http://127.0.0.1:8080/')
    
    # Get the user input
    name = input('Enter your name: ')
    
    # Print the name to the screen
    print('Hello, ' + name + '!')
    
    # Close the webpage
    webbrowser.close