#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers. """    
    
    count = 0
    
    while True:
        count += 1
        
        if count == 10:
            break
        
        print('#', end='')
        
        time.sleep(1)
        
    print('Done')
