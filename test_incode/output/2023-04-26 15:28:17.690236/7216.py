#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or calculates words. """    
    
    words = []
    
    # Open a text file containing words and add them to the list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
            
    # Print the list of words to the user
    print('\n'.join(words))
    
    # Open a web page and display the list of words to the user
    webbrowser.open('words.html')
    
    # Calculate and print the list of words to the user
    words = [word for word in words if word != '']
    
    print('\n'.join(words))
    
    # Close the web page
    webbrowser.close('words.html')
    
    # Close the text file
    with open('words.txt', 'w') as f:
        f.write('\n'.join(words))
        
    # Close the file
