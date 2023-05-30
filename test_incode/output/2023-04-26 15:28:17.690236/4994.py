#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    # Open a web browser and open a page to allow users to enter data.
    browser = webdriver.Firefox()
    browser.implicitly_wait(30)
    browser.