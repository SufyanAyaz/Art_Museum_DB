
import mysql.connector


def DataEntry():
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

    print("Welcom Employee to Data Entry")

    i = 0
    while (i == 0):
        print("Would you like to Insert new data, Update existing data, or delete existing data")
        print("1-INSERT")
        print("2-UPDATE")
        print("3-DELETE")
        print("4-LOOKUP INFORMATION")
        print("5-QUIT")
        selection = input(
            "Please input one of the three options (1 , 2, 3, or 4): ")
        if (selection == '1'):
            print("What is the name of the table you wish to insert data into")
            table_name = input("Please input the table name here: ")
            Insert = "INSERT INTO " + table_name
            Insert += " "

            column_num = input("How many columns do you wish to update: ")

            while column_num.isnumeric() == False:
                print("Invalid input")
                column_num = input(
                    "Enter the number of columns you would like to insert: ")
            column_num = int(column_num)
            val = 0
            copy = column_num
            while (val == 0):
                Insert += "("
                if (copy > 1):
                    col_name = input(
                        "what is the name of the colum you wish to add data into(If values are unknown or you wish to make the values NULL don't name the column: ")
                    Insert += col_name + ", "
                    copy = copy - 1
                if copy == 1:
                    col_name = input(
                        "what is the name of the colum you wish to add data into(If values are unknown or you wish to make the values NULL don't name the column): ")
                    Insert += col_name + ")"
                    val = 1
            Insert += " VALUES "
            Insert += "('"
            while (val == 1):
                if (column_num > 1):
                    col_name = input("what is the value you are adding: ")
                    Insert += col_name + "', '"
                    column_num = column_num - 1
                if column_num == 1:
                    col_name = input("what is the value you are adding: ")
                    Insert += col_name + "')"
                    val = 2
            Insert += ";"

            try:

                cursor.execute(f'{Insert}')
                cnx.commit()
                print("The values have been Inserted")

            except mysql.connector.Error as e:
                print("AN ERROR WAS DETTECTED ERROR SHOWN BELLOW")
                print(e)

            except:
                print(
                    "An unkown error was detected in your Input Statement! Please Try Again!")

        elif (selection == '2'):
            print("You have selected to update an existing table")
            update = "UPDATE "

            table_name = input(
                "What is the Name of the table you wish to update?\n")
            update += table_name
            update += " SET "

            check = 1
            while (check == 1):
                colum_number = input(
                    "How many columns do you wish to update?\n")

                if (colum_number.isnumeric() == True):
                    check = 0
                else:
                    print("You did not enter a number please try agin")

            colum_number = int(colum_number)
            while (colum_number > 0):
                colum_name = input(
                    "What is the name of the column you wish to update\n")
                colum_new_value = input(
                    "What is the new value you wish to set for this column\n")
                update += colum_name
                update += " = "
                update += "'"
                update += colum_new_value
                update += "'"
                if (colum_number > 1):
                    update += ", "
                colum_number = colum_number - 1

            where_conditions = []
            if_where = input(
                "Does your query statement have any 'WHERE' conditions (enter either 'Y' for yes or anything esle for No): ")
            if (if_where == 'Y' or if_where == 'y'):
                num_where_conditions = int(
                    input("How many 'WHERE' conditions does your statement have: "))
                for w_cond in range(num_where_conditions):
                    w_cond = input(
                        "Enter a 'WHERE' condition (be sure to include any necessary aliases in front of any attributes): ")
                    where_conditions.append(w_cond)

                update += ' ' + "WHERE" + ' ' + \
                    (' AND '.join(where_conditions))
                update += ';'
            else:
                update += ";"

            try:
                cursor.execute(f'{update}')
                cnx.commit()
                print("The values have been Inserted")

            except mysql.connector.Error as e:
                print("AN ERROR WAS DETTECTED ERROR SHOWN BELLOW")
                print(e)

            except:
                print(
                    "An unknown error was detected in your Input Statement! Please Try Again!")

        elif (selection == '3'):
            print("Choose one of the folowing:")
            print("Delete an existing value (Enter 1):")
            print("Delete all values without deleting the table (Enter 2):")

            inp = input("Choose an option:")
            while (inp != '1') and (inp != '2'):
                print('Invalid input. Please try again:')
                inp = input("Choose an option again:")

            table1 = input("Enter the table you would like to delete from:")
            table = table1.lower()

            if (inp == '1'):
                column = input(
                    "Enter the column you would like to delete from:")
                record = input("Enter the value you would like to delete:")
                if (record == 'NULL') or (record == 'Null') or (record == 'null'):
                    record = None
                    tab1 = "DELETE FROM "+table.upper()+" WHERE "+column+"=(%s)"
                    tup1 = (record,)

                    try:

                        cursor.execute(tab1, tup1)
                        cnx.commit()
                        print("Your Delete Statement was successfully executed!")
                    except mysql.connector.Error as e:
                        print("AN ERROR WAS DETTECTED ERROR SHOWN BELLOW")
                        print(e)

                    except:
                        print(
                            "An unknown error was detected in your Delete Statement! Please Try Again!")

                else:
                    tab1 = "DELETE FROM "+table.upper()+" WHERE "+column+"='"+record+"';"
                    try:

                        cursor.execute(tab1)
                        cnx.commit()
                        print("Your Delete Statement was successfully executed!")

                    except mysql.connector.Error as e:
                        print("AN ERROR WAS DETTECTED ERROR SHOWN BELLOW")
                        print(e)

                    except:
                        print(
                            "An unknown error was detected in your Delete Statement! Please Try Again!")

            else:
                tab1 = "DELETE FROM "+table.upper()+";"

                try:

                    cursor.execute(tab1)
                    cnx.commit()
                    print("Your Delete Statement was successfully executed!")

                except mysql.connector.Error as e:
                    print("AN ERROR WAS DETTECTED ERROR SHOWN BELLOW")
                    print(e)

                except:
                    print(
                        "An unknown error was detected in your Delete Statement! Please Try Again!")

        elif (selection == '4'):
            table_name = input(
                "What is the name of the table you wish to view: ")
            Select = "SELECT * FROM " + table_name + ";"

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

        elif (selection == '5'):
            return
        else:
            print("Incorrect Selection please try again")
