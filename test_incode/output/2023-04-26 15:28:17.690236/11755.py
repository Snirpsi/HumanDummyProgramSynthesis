#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or enumerates user input. """    
    
    # Define a function to add words to our dictionary
    def add_words(words):
        
        # Create a dictionary to hold our words
        words_dict = {}
        
        # Iterate through the words and add them to our dictionary
        for word in words:
            
            # If the word is not already in the dictionary, add it to the dictionary
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
                
        # Return the dictionary with the new words
        return words_dict
    
    # Define a function to enumerate our input
    def enumerate_words(words):
        
        # Create a dictionary to hold our words
        words_dict = {}
        
        # Iterate through the words and add them to our dictionary
        for word in words:
            
            # If the word is not already in the dictionary, add it to the dictionary
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
                
        # Return the dictionary with the new words
        return words_dict
    
    # Define a function to print our dictionary
    def print_dictionary(words_dict):
        
        # Iterate through the words and print them
        for word in words_dict:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our input
    def print_input(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word)
    
    # Define a function to print our output
    def print_output(words_dict):
        
        # Iterate through the words and print them
        for word in words_dict:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our output
    def print_output(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our output
    def print_output(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our output
    def print_output(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our output
    def print_output(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word, "\t", words_dict[word])
    
    # Define a function to print our output
    def print_output(words):
        
        # Iterate through the words and print them
        for word in words:
            print(word, "\t", words_dict[word])
