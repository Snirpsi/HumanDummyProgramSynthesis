#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or multiplyes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <nums> [nums] [nums]" % sys.argv[0])
        sys.exit(0)
    
    nums = sys.argv[1:]
    
    if len(nums) == 1:
        nums = nums * 2
    
    numbers = map(int, nums)
    
    print("%s x %s = %s" % (numbers[0], numbers[1], numbers[0] * numbers[1]))
    
