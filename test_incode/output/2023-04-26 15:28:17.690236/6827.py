#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or calculates words. """    
    
    # Open user input
    words = []
    
    # Read user input
    while True:
        word = input("Enter a word: ")
        
        # Check if word is valid
        if word and word not in words:
            words.append(word)
        else:
            print("Invalid word. Try again.")
    
    # Print results
    print("The words are:")
    for word in words:
        print(word)
    
    # Calculate results
    total = 0
    
    # Iterate through words and add their values
    for word in words:
        total += word.count("a")
    
    print("The total is", total)
    
