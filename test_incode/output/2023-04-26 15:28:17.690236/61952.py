#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or opens a list of numbers. """    
    
    # Open a web page with default values
    webbrowser.open('http://127.0.0.1:8000')
    
    # Open a web page with user input
    webbrowser.open('http://127.0.0.1:8000?a=5')
    
    # Open a web page with user input and a list
    webbrowser.open('http://127.0.0.1:8000?a=5&b=