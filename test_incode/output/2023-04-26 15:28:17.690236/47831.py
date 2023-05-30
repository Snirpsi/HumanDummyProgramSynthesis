#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        print("Welcome to the endless loop!")
        print("Please type in a command:")
        print("\t1. Add a new user")
        print("\t2. Add a new group")
        print("\t3. Add a new permission")
        print("\t4. Add a new role")
        print("\t5. Quit")
        command = input("Command: ")
        if command == "1":
            user = input("Username: ")
            group = input("Group: ")
            permission = input("Permission: ")
            role = input("Role: ")
            
            user = user.capitalize()
            group = group.capitalize()
            permission = permission.capitalize()
            role = role.capitalize()
            
            user = User(user, group, permission, role)
            
            print("User {} has been added.".format(user))
        elif command == "2":
            user = input("Username: ")
            group = input("Group: ")
            permission = input("Permission: ")
            role = input("Role: ")
            
            user = user.capitalize()
            group = group.capitalize()
            permission = permission.capitalize()
            role = role.capitalize()
            
            group = Group(group, user, permission, role)
            
            print("Group {} has been added.".format(group))
        elif command == "3":
            user = input("Username: ")
            group = input("Group: ")
            permission = input("Permission: ")
            role = input("Role: ")
            
            user = user.capitalize()
            group = group.capitalize()
            permission = permission.capitalize()
            role = role.capitalize()
            
            permission = Permission(permission, user, role)
            
            print("Permission {} has been added.".format(permission))
        elif command == "4":
            user = input("Username: ")
            group = input("Group: ")
            permission = input("Permission: ")
            role = input("Role: ")
            
            user = user.capitalize()
            group = group.capitalize()
            permission = permission.capitalize()
            role = role.capitalize()
            
            role = Role(role, user, permission)
            
            print("Role {} has been added.".format(role))
        elif command == "5":
            break
        else:
            print("Invalid command.")
            
