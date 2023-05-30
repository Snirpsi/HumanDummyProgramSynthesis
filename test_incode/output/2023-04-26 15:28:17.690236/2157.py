#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or enumerates a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port number or a list of numbers: "))
            if port > 0:
                ports = [port]
            else:
                ports = range(port)
            for port in ports:
                port = str(port)
                ports.append(port)
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Invalid input. Try again.")
            continue
        except IndexError:
            print("Invalid input. Try again.")
            continue
        except ValueError as ve