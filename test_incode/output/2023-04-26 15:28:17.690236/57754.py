#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    words = []
    
    # Open the wordlist
    with open('wordlist.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Open the word list in a browser
    browser = Browser()
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello&word=world')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello&word=world&word=hello')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello')
    
    # Open the word list in a browser
    browser.open('http://localhost:8000/wordlist.html?word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=hello&word=world&word=