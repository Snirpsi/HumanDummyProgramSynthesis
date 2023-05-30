#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    # Open a web browser window and display a wordlist
    browser = Browser()
    browser.open('http://wordlists.org')
    
    # Wait for user input before continuing
    browser.wait_for_