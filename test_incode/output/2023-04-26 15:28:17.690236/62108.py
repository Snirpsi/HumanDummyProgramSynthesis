#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or opens user input. """    
    
    # Parse command line arguments
    args = parse_args()
    
    # Open user input if necessary
    if args.open:
        open_input()
    
    # Multiply words in list
    multiply(args.words)
    
    # Close user input if necessary
    if args.close:
        close_input()
    
    # 