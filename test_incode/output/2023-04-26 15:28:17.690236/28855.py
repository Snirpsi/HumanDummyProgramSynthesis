#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or removes fruits. """    
    
    web = web.Application([
        (r'/', MainPage),
        (r'/remove', RemoveFruits),
        (r'/add', AddFruits),
        (r'/fruits', Fruits),
        (r'/fruits/<fruit>/<quantity>', Fruit),
        (r'/fruits/<fruit>/<quantity>/remove', RemoveFruit),
        (r'/fruits/<fruit>/<quantity>/add', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>', AddFruit),
        (r'/fruits/<fruit>/<quantity>/add/<quantity>/<quantity>/<quantity>/<quantity>/<quantity>/<