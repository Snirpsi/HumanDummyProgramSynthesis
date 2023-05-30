#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or converts fruits. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that enumerates a list of numbers or converts fruits.')
    parser.add_argument('numbers', metavar='numbers', nargs='+', help='A list of numbers to enumerate.')
    args = parser.parse_args()
    
    # Enumerate numbers
    numbers = args.numbers
    
    # Convert numbers
    numbers = convert_numbers(numbers)
    
    # Print results
    print('\n'.join(numbers))
    
    # Start webserver
    webserver.run(host='0.0.0.0', port=8080)
    
