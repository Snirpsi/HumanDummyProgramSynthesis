#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: remove_numbers.py <file>')
        sys.exit()
    
    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip()
            
            if line:
                line = line.split()
                
                if len(line) > 1:
                    line = line[1:]
                    
                    line[0] = str(int(line[0]))
                    
                    line = ''.join(line)
                    
                    print(' '.join(line))
                    
                else:
                    print(' '.join(line))
                    
            else:
                print(' '.join(line))
                
