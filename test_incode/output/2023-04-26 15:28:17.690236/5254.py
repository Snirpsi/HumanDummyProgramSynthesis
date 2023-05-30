#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    # Open the wordlist
    with open('wordlist.txt', 'r') as f:
        words = f.read().splitlines()
        
    # Open the webpage
    webpage = open('wordlist.html', 'r')
    
    # Open the wordlist
    with open('wordlist.html', 'w') as f:
        f.write('<html><body>')
        
        # Open the wordlist
        for word in words:
            f.write('<a href="?word={}">{}</a><br>'.format(word, word))
        
        # Close the wordlist
        f.write('</body></html>')
        
    # Close the webpage
    webpage.close()
    
    # Open the webpage
    webpage = open('wordlist.html', 'r')
    
    # Open the wordlist
    with open('wordlist.html', 'w') as f:
        f.write('<html><body>')
        
        # Open the wordlist
        for word in words:
            f.write('<a href="?word={}">{}</a><br>'.format(word, word))
        
        # Close the wordlist
        f.write('</body></html>')
        
    # Close the webpage
    webpage.close()
    
    # Open the webpage
    webpage = open('wordlist.html', 'r')
    
    # Open the wordlist
    with open('wordlist.html', 'w') as f:
        f.write('<html><body>')
        
        # Open the wordlist
        for word in words:
            f.write('<a href="?word={}">{}</a><br>'.format(word, word))
        
        # Close the wordlist
        f.write('</body></html>')
        
    # Close the webpage
    webpage.close()
    
    # Open the webpage
    webpage = open('wordlist.html', 'r')
    
    # Open the wordlist
    with open('wordlist.html', 'w') as f:
        f.write('<html><body>')
        
        # Open the wordlist
        for word in words:
            f.write('<a href="?word={}">{}</a><br>'.format(word, word))
        
        # Close the wordlist
        f.write('</body></html>')
        
    # Close the webpage
    webpage.close()
    
    # Open the webpage
    webpage = open('wordlist.html', 'r')
    
    # Open the wordlist
    with open('wordlist.html', 'w') as f:
        f.write('<html><body>')
        
        # Open the wordlist
        for word in words:
            f.write('<a href="?word={}">{}</a><br>'.format(word, word))
        
        # Close the wordlist
        f.write('</body></html>')
        
    # Close the webpage
    webpage.close()
    
    # 