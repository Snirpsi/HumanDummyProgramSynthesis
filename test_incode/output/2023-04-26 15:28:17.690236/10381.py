#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or stores all ports. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="A minimal webserver that removes a list of numbers or stores all ports.")
    parser.add_argument("ports", help="The ports to remove.")
    args = parser.parse_args()
    ports = args.ports.split(',')
    
    # Run the server
    run(ports)

<|/ file source=github dstars=1 |>