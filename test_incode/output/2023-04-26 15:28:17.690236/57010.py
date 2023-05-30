#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Add words to the list
    words.append("hello")
    words.append("world")
    
    # Print the list
    print(words)
    
    # Send the list to the browser
    send_to_browser(words)
    
    # 