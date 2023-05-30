#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input or returns words. """    
    while True:
        line = input('> ')
        if line == 'exit':
            break
        line = line.strip()
        if line == 'help':
            print('''
            Convert words to numbers and print them out. 
            
            Usage: python words_to_numbers.py [options]
            ''')
        elif line == 'numbers':
            print('''
            Convert words to numbers and print them out. 
            
            Usage: python words_to_numbers.py [options]
            ''')
        else:
            print(line_to_number(line))
    
