#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addlist.py <list>")
        sys.exit()
    
    list1 = []
    list2 = []
    
    for arg in sys.argv[1:]:
        
        try: 
            list1.append(int(arg))
        except ValueError:
            print("Error: invalid list number")
            sys.exit()
        
        try: 
            list2.append(int(arg))
        except ValueError:
            print("Error: invalid list number")
            sys.exit()
        
    list1.sort()
    list2.sort()
    
    print(list1 + list2)
    
