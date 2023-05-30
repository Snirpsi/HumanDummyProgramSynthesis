#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or enumerates a list of numbers. """    
    
    words = ['cat', 'dog', 'mouse']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        try:
            
            choice = input('Enter a number: ')
            
            if choice == 'exit':
                
                break
                
            elif choice == '1':
                
                numbers[0] = numbers[0] + 1
                
            elif choice == '2':
                
                numbers[1] = numbers[1] + 1
                
            elif choice == '3':
                
                numbers[2] = numbers[2] + 1
                
            elif choice == '4':
                
                numbers[3] = numbers[3] + 1
                
            elif choice == '5':
                
                numbers[4] = numbers[4] + 1
                
            elif choice == '6':
                
                numbers[5] = numbers[5] + 1
                
            elif choice == '7':
                
                numbers[6] = numbers[6] + 1
                
            elif choice == '8':
                
                numbers[7] = numbers[7] + 1
                
            elif choice == '9':
                
                numbers[8] = numbers[8] + 1
                
            elif choice == '10':
                
                numbers[9] = numbers[9] + 1
                
            else:
                
                print('Invalid choice.')
                
        except KeyboardInterrupt:
            
            print('\nExiting program.')
            
            break
            
        except EOFError:
            
            print('\nExiting program.')
            
            break
            
        except IndexError:
            
            print('\nExiting program.')
            
            break
            
        except TypeError:
            
            print('\nExiting program.')
            
            break
            
        except NameError:
            
            print('\nExiting program.')
            
            break
            
        except TypeError:
            
            print('\nExiting program.')
            
            break
            
        except IndexError:
            
            print('\nExiting program.')
            
            break
            
        except NameError:
            
            print('\nExiting program.')
            
            break
            
        except TypeError:
            
            print('\nExiting program.')
            
            break
            
        except IndexError:
            
            print('\nExiting program.')
            
            break
            
        except NameError:
            
            print('\nExiting program.')
            
            break
            
        except TypeError:
            
            print('\nExiting program.')
            
            break
            
        except IndexError:
            
            print('\nExiting program.')
            
            break
            
        except NameError:
            
            print('\nExiting 