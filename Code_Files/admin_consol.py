import mysql.connector


def admin_view():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    cnx = mysql.connector.connect(

        user=username,
        password=password,
        host="127.0.0.1",
        port=3306)

    cursor = cnx.cursor()
    cursor.execute("use artmuseum")

    check = 0
    print("Welcom DB Admin")
    while (check == 0):
        print("In order to proceed please select what you wish to do:")
        print("1-Add Users")
        print("2-Edit Users")
        print("3-Block Users")
        print("4-Make Changes To The Database")
        print("5-Query The Database")
        print("6-quit")

        selection = input(
            "please type 1, 2, 3, 4, 5 or 6 to secet your role: ")
        if selection == '1':
            print("You have chosen to add a user")
            loop = 0
            while (loop == 0):
                name = input(
                    "What is the username of the user you wish to add: ")
                password = input("What is there password: ")
                create_user = "DROP USER IF EXISTS " + name + "@localhost;"
                create_user += " CREATE USER " + name + \
                    "@localhost IDENTIFIED WITH mysql_native_password BY '" + password + "'; "
                print("Which role is to be gratned to this user")
                print("1-Admin")
                print("2-Data Entry users")
                print("3-End User")
                pick = input()
                if (pick == '1'):
                    create_user += "GRANT db_admin@localhost TO " + name + "@localhost;"
                    loop = 1
                elif (pick == '2'):
                    create_user += "GRANT entry_access@localhost TO " + name + "@localhost;"
                    loop = 1
                elif (pick == '3'):
                    create_user += "GRANT read_access@localhost TO " + name + "@localhost;"
                    loop = 1
                else:
                    print("Incorrect selection try again")
            create_user += " SET DEFAULT ROLE ALL TO " + name + "@localhost;"
            cursor.execute(create_user)
            cnx.commit()
            print("The user has been added")

        elif selection == '2':
            print("You have chosen to edit an existing user")

            loop = 0
            while (loop == 0):
                name = input(
                    "What is the username of the user you wish to edit: ")
                print("What would you like to edit about the user")
                print("1-Change password")
                print("2-Delete user")
                print("3-Change role")
                pick = input()

                if (pick == '1'):
                    password = input(
                        "What is the new password you wish to set: ")
                    create_user = "ALTER USER " + name + \
                        "@localhost IDENTIFIED WITH mysql_native_password BY '" + password + "';"
                    try:
                        cursor.execute(f'{create_user}')
                        cnx.commit()
                        print("The users password has been changed")
                    except:
                        print("An error was detected! Please Try Again!")
                    loop = 1

                elif (pick == '2'):
                    remove = 0
                    while (remove == 0):
                        print(
                            "Are you sure you wish to deleate this user. (Y for yes) (N for no)")
                        varify = input()
                        if (varify == 'Y' or varify == 'y'):
                            delete = "DROP USER IF EXISTS " + name + "@localhost;"
                            remove = 1
                            try:
                                cursor.execute(f'{remove}')
                                cnx.commit()
                                print("The user has been removed")
                            except:
                                print("An error was detected! Please Try Again!")
                            loop = 1

                        elif (varify == 'N' or varify == 'n'):
                            remove = 1
                            loop = 1
                        else:
                            print("Make a correct selection")

                elif (pick == '3'):
                    loop = 0
                    while (loop == 0):
                        print("Which role is to be gratned to this user")
                        print("1-Admin")
                        print("2-Data Entry users")
                        print("3-End User")
                        pick = input()
                        if (pick == '1'):
                            role = "GRANT db_admin@localhost TO " + name + "@localhost;"
                            loop = 1
                        elif (pick == '2'):
                            role = "GRANT entry_access@localhost TO " + name + "@localhost;"
                            loop = 1
                        elif (pick == '3'):
                            role = "GRANT read_access@localhost TO " + name + "@localhost;"
                            loop = 1
                        else:
                            print("Incorrect selection try again")

                    try:
                        cursor.execute(f'{role}')
                        cnx.commit()
                        print("The role has been changed")
                    except:
                        print("An error was detected! Please Try Again!")

                else:
                    print("Incorrect selection please try again")
        elif selection == '3':
            print("You have chosen to Block a user")
            name = input(
                "What is the username of the user you wish to block: ")
            loop = 0
            while (loop == 0):
                print("What is the role gratned to this user")
                print("1-Admin")
                print("2-Data Entry users")
                print("3-End User")
                pick = input()
                if (pick == '1'):
                    block = "DENY db_admin@localhost FROM " + name + "@localhost;"
                    loop = 1
                elif (pick == '2'):
                    block = "DENY entry_access@localhost FROM " + name + "@localhost;"
                    loop = 1
                elif (pick == '3'):
                    block = "DENY read_access@localhost FROM " + name + "@localhost;"
                    loop = 1
                else:
                    print("Incorrect selection try again")
            cursor.execute(f'{block}')
            cnx.commit()
            print("The user has been blocked")

        elif selection == '4':
            loop2 = 0
            print("You have chosen to make changes to the Database")
            while (loop2 == 0):
                print("Would you like to make changes to the database using")
                print("1-SQL command")
                print("2-SQL File")
                choice = input()
                if (choice == '1'):
                    admin_change = input(
                        "Write your MYSQL statement in a proper fromat: \n")
                    try:
                        cursor.execute(f'{admin_change}')
                        cnx.commit()
                        print("Changes have been made to the database")
                    except mysql.connector.Error as e:
                        print(e)
                    except:
                        print("An error was detected! Please Try Again!")
                    loop2 = 1

                if (choice == '2'):
                    print("Please enter your file path or file name: ")
                    file = input()
                    fd = open(file, 'r')
                    sqlFile = fd.read()
                    fd.close()
                    sqlCommands = sqlFile.split(';')

                    for command in sqlCommands:
                        try:
                            if command.strip() != '':
                                cursor.execute(command)
                        except mysql.connector.Error as e:
                            print(e)
                        except:
                            print("Error detected")

                else:
                    print("Incorrect selection please try again")
                n = 0
                while (n == 0):
                    print(
                        "Would you like to see the changes you made (Y for yes N for no)")
                    decide = input()
                    if decide == "Y" or decide == "y":
                        table_name = print(
                            "What is the name of the table you wish to view: ")
                        Select = "SELECT * FROM " + table_name

                        try:
                            cursor.execute(f'{Select}')

                            attribute_names = cursor.column_names
                            attributes_size = len(attribute_names)

                            for i in range(attributes_size):
                                print(f'{attribute_names[i]:<25}', end='')
                            print()
                            print((attributes_size * 25) * '-')

                            information = cursor.fetchall()
                            information_size = len(information)

                            for j in range(information_size):
                                for k in range(len(information[j])):
                                    string = str(information[j][k])
                                    print(f'{string:<25}', end='')
                                print()

                        except mysql.connector.Error as e:
                            print(e)
                        except:
                            print("Unknown error occurred please try again")
                    elif decide == "N" or decide == "n":
                        n = 1
                    else:
                        print("incorrect selection, try again")

        elif selection == "5":
            loop3 = 0
            print("You have chosen to query the Database")
            while (loop3 == 0):
                admin_query = input(
                    "Write your MYSQL statement in a proper fromat: \n")
                try:
                    cursor.execute(f'{admin_query}')

                    attribute_names = cursor.column_names
                    attributes_size = len(attribute_names)

                    for i in range(attributes_size):
                        print(f'{attribute_names[i]:<25}', end='')
                    print()
                    print((attributes_size * 25) * '-')

                    information = cursor.fetchall()
                    information_size = len(information)

                    for j in range(information_size):
                        for k in range(len(information[j])):
                            string = str(information[j][k])
                            print(f'{string:<25}', end='')
                        print()

                except mysql.connector.Error as e:
                    print(e)
                except:
                    print("Unknown error occurred please try again")
                loop3 = 1

        elif selection == "6":
            print("Quiting the admin program")
            check = 1
            return

        else:
            print("You did not make a correct selection please try again")
