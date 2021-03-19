"""Contact book saved in sqlite database."""

import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)


def view_contacts(conn):
    """Return a list of contacts."""
    c = conn.cursor()
    c.execute("SELECT * from contacts;")
    return c.fetchall()


def add_contact(conn):
    """Add contact to database."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    c = conn.cursor()
    c.execute("INSERT INTO contacts(firstName,lastName,phoneNumber) \
        VALUES(?,?,?)", (first_name, last_name, phone_number))
    conn.commit()


def delete_contact(conn):
    """Delete contact from database."""
    user_delete = input("Enter contact index to delete: ")
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (user_delete,))
    conn.commit()


def search_contact(conn):
    """Search for contact in database."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE firstName LIKE ?\
                AND lastName LIKE ?",
              ('%' + first_name + '%', '%' + last_name + '%',))
    return c.fetchall()


def print_menu():
    print("[1] Add contact")
    print("[2] View contacts")
    print("[3] Search contact")
    print("[4] Delete contact")


def menu():
    print_menu()

    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Enter a number instead of letter. ")
        menu()

    while option != 0:
        if option == 1:
            add_contact(conn)
        elif option == 2:
            print(view_contacts(conn))
        elif option == 3:
            contacts_found = search_contact(conn)
            if not contacts_found:
                print('No contacts found')
            else:
                print(contacts_found)

        elif option == 4:
            delete_contact(conn)
        else:
            print("Invalid option")
            menu()

        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Enter a number instead of letter. ")
            menu()


# Load database
db_file = "contacts.db"

sqlite_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts (
                                        id integer primary key autoincrement,
                                        firstName text,
                                        lastName text ,
                                        phoneNumber text
                                    ); """

if __name__ == '__main__':
    conn = create_connection(db_file)
    create_table(conn, sqlite_create_contacts_table)

    menu()
