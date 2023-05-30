#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    # Read numbers from stdin and store them in nums
    nums = []
    for _ in range(int(input())):
        nums.append(int(input()))
    
    # Print the numbers in nums
    for num in nums:
        print(num)
        
    # Print the sum of the numbers in nums
    print(sum(nums))
    
    # Print the average of the numbers in nums
    print(sum(nums) / len(nums))
    
    # Print the median of the numbers in nums
    print(sorted(nums)[len(nums) / 2])
    
    # Print the modes of the numbers in nums
    print(sorted(nums)[