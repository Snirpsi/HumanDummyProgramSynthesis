#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and stores words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # Loop until the user hits Ctrl-C
    try:
        while True:
            multiplier = int(input('Enter a number: '))
            
            # Loop through each word in the list
            for word in words:
                # Multiply the number by the word
                word = word * multiplier
                
                # Print the word and the multiplied number
                print('{} x {} = {}'.format(word, multiplier, word))
            
            # Print the final result
            print('The multiplication was {}'.format(words[-1]))
            
            # Pause the program for 1 second
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Stop the program if Ctrl-C is hit
        print('\nExiting...')
        
        # Stop the program from printing anything to the screen
        sys.stdout.flush()
        
        # Stop the program from printing anything to the screen
        sys.stderr.flush()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()
        
        # Stop the program from printing anything to the screen
        sys.stdout.close()
        
        # Stop the program from printing anything to the screen
        sys.stderr.close()