#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    # read user input
    filename = input('Enter the name of the file you want to convert: ')
    
    # read file content
    with open(filename, 'r') as file:
        content = file.read()
        
    # convert file content
    content = content.replace('\n', ' ')
    content = content.replace('\r', ' ')
    content = content.strip()
    
    # write converted file
    with open(filename, 'w') as file:
        file.write(content)
        
    print('Done!')
