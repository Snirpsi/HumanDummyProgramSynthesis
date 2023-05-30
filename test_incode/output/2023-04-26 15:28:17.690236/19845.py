#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that adds a list of numbers')
    parser.add_argument('numbers', metavar='N', type=str, nargs='+', help='A list of numbers')
    args = parser.parse_args()
    
    # Start webserver
    server = WebServer()
    server.run(args.numbers)

<|/ file filename=webserver.py |>