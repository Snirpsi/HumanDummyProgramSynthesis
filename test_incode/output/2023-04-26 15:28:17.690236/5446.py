#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or removes words. """    
    
    # Parse command line arguments
    args = parse_args()
    
    # Remove words from the list
    remove_words(args.wordlist)
    
    # Remove words from the file
    remove_words(args.file)
    
    # Show the result
    print("Done.")
    
    # Stop the server
    stop_server()
    
