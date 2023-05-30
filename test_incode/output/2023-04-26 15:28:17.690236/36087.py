#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words and converts fruits. """    
    
    words = []
    
    # Open the file words.txt
    with open('words.txt', 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        words.append(line.strip())
        
    # Convert each word to lowercase
    words = [word.lower() for word in words]
    
    # Print the converted words
    for word in words:
        print(word)
        
    # Close the file
    file.close()
    
