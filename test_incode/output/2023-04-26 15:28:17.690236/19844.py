#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and opens numbers. """    
    
    # Define the list of words and open numbers
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    # Iterate over words and open numbers
    for word in words:
        number = int(word)
        
        # Print the number
        print('The number is', number)
        
        # Close the webserver
        