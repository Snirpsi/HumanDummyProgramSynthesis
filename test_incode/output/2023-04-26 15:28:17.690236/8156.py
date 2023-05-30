#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Remove words from a text file.')
    parser.add_argument('file', metavar='FILE', help='The text file to remove words from.')
    args = parser.parse_args()
    
    # Remove words from file
    with open(args.file, 'r') as file:
        words = file.read().splitlines()
        
    # Remove words from file
    with open(args.file, 'w') as file:
        for word in words:
            if word not in words:
                file.write(word)
                file.write('\n')
                
    print('Done!')
    
