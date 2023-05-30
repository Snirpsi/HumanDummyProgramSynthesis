#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or stores a list of numbers. """    
    
    numbers = []
    
    while True:
        
        try:
            
            number = int(input('Enter a number: '))
            
            if number in numbers:
                
                print('This number has already been entered.')
                
            else:
                
                numbers.append(number)
                
                print('The number has been added to the list.')
                
        except EOFError:
            
            print('The list has been completed.')
            
            break
            
        except KeyboardInterrupt:
            
            print('The list has been completed.')
            
            break
            
        except ValueError as e:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except IndexError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except NameError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except EOFError:
            
            print('The list has been completed.')
            
            break
            
        except KeyboardInterrupt:
            
            print('The list has been completed.')
            
            break
            
        except ValueError as e:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except EOFError:
            
            print('The list has been completed.')
            
            break
            
        except KeyboardInterrupt:
            
            print('The list has been completed.')
            
            break
            
        except ValueError as e:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except EOFError:
            
            print('The list has been completed.')
            
            break
            
        except KeyboardInterrupt:
            
            print('The list has been completed.')
            
            break
            
        except ValueError as e:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except EOFError:
            
            print('The list has been completed.')
            
            break
            
        except KeyboardInterrupt:
            
            print('The list has been completed.')
            
            break
            
        except ValueError as e:
            
            print('Invalid input. Please try again.')
            
            continue
            
        except TypeError:
            
            print('Invalid input. Please try again.')
            