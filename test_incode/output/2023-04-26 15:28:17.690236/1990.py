#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and converts words. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    fruits_as_strings = []
    for fruit in fruits:
        fruits_as_strings.append(fruit)
    
    fruits_as_strings_as_ints = []
    for fruit in fruits:
        fruits_as_strings_as_ints.append(int(fruit))
    
    fruits_as_strings_as_floats = []
    for fruit in fruits:
        fruits_as_strings_as_floats.append(float(fruit))
    
    fruits_as_strings_as_strs = []
    for fruit in fruits:
        fruits_as_strings_as_strs.append(str(fruit))
    
    fruits_as_strings_as_bools = []
    for fruit in fruits:
        fruits_as_strings_as_bools.append(bool(fruit))
    
    fruits_as_strings_as_lists = []
    for fruit in fruits:
        fruits_as_strings_as_lists.append(list(fruit))
    
    fruits_as_strings_as_tuples = []
    for fruit in fruits:
        fruits_as_strings_as_tuples.append(tuple(fruit))
    
    fruits_as_strings_as_sets = []
    for fruit in fruits:
        fruits_as_strings_as_sets.append(set(fruit))
    
    fruits_as_strings_as_frozensets = []
    for fruit in fruits:
        fruits_as_strings_as_frozensets.append(frozenset(fruit))
    
    fruits_as_strings_as_sets_as_frozensets = []
    for fruit in fruits:
        fruits_as_strings_as_sets_as_frozensets.append(set(fruit).frozenset())
    
    fruits_as_strings_as_sets_as_lists = []
    for fruit in fruits:
        fruits_as_strings_as_sets_as_lists.append(set(fruit).list())
    
    fruits_as_strings_as_sets_as_tuples = []
    for fruit in fruits:
        fruits_as_strings_as_sets_as_tuples.append(set(fruit).tuple())
    
    fruits_as_strings_as_sets_as_sets = []
    for fruit in fruits:
        fruits_as_strings_as_sets_as_sets.append(set(fruit).set())
    
    fruits_as_strings_as_sets_as_frozensets = []
    for fruit in fruits:
        fruits_as_string