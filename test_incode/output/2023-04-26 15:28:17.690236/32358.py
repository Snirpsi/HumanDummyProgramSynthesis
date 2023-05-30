#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['cat', 'dog', 'bird', 'mouse']
    
    while True:
        
        # Print the words in the list one by one
        for word in words:
            print(word)
            
        # Pause for a second
        time.sleep(1)
        
        # Exit the loop
        break
        
