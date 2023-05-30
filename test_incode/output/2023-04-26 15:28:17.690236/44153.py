#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or stores numbers. """    
    
    # Print the numbers or store them
    if sys.argv[1] == 'print':
        print(*map(int, input().split()))
    elif sys.argv[1] == 'store':
        numbers = map(int, input().split())
        print(*numbers)
    else:
        print('Invalid command')
        
