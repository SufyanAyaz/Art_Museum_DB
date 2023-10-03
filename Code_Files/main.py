import mysql.connector
from admin_consol import *
from DataEntry import *
from enduser import *
from guest import *


def main():

    print("Please Enter Your Root Username and Password!")
    user_name = input("Root Username: ")
    pass_word = input("Root Password: ")

    cnx = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user=user_name,
        password=pass_word)

    cursor = cnx.cursor()
    cursor.execute("use artmuseum")

    print("Welcome to the Art Museum Database!")
    print("In order to proceed please select your role from the list below:")
    print("1 - Database Admin")
    print("2 - Data Entry User")
    print("3 - End User")
    print("4 - Guest")

    role = int(
        input("Please enter the number corresponding to your role: "))

    if (role == 1):
        admin_view()
    elif (role == 2):
        DataEntry()
    elif (role == 3):
        end_user_view()
    else:
        guest_view()

    print("Thank You for Visiting the Art Museum Database! Please Come Again Soon!")


if __name__ == '__main__':  # Main program is being run.
    main()  # Calling on "main()" function.
