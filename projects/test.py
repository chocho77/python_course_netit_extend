# Module Import
import mariadb
import sys

# https://mariadb.com/kb/en/mariadb-connector-python/

# https://pypi.org/project/tonydbc/

def return_choice(choice: str) -> bool:
     if choice == 'y':
          return True
     return False

     
     

# Create List of Contacts
def create_contacts(cur):
        while True:
             first_name = input("Enter first name : ")
             last_name = input("Enter last name : ")
             email = input("Enter email :")
             cur.execute(f"INSERT INTO contacts(first_name, last_name, email)\
                     VALUES('{first_name}', '{last_name}', '{email}')")
             choice = input("Continue: (y/n)")
             if return_choice(choice):
                  pass
             else:
                  break
                  
                  
# Print List of Contacts
def print_contacts(cur):
     """Retrieves the list of contacts from the database and prints to stdout"""

     # Initialize Variables
     contacts = []

     # Retrieve Contacts
     cur.execute("SELECT first_name, last_name, email FROM contacts")

     # Prepare Contacts
     for (first_name, last_name, email) in cur:
        contacts.append(f"{first_name} {last_name} <{email}>")

     # List Contacts
     print("\n".join(contacts))

if __name__ == '__main__':
     # Instantiate Connection
    try:
        conn = mariadb.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="xQNM#2@yKL")
        query = 'USE chocho'
        #query_one = "CREATE TABLE contacts(first_name VARCHAR(50),\
        #                                    last_name VARCHAR(50), \
        #                                    email VARCHAR(50))"
        
        

        #query_two = f"INSERT INTO contacts(first_name, last_name, email)\
        #            VALUES('{first_name}', '{last_name}', '{email}')"
        
    
        # Instantiate Cursor
        cur = conn.cursor()
        cur.execute(query)
        #cur.execute(query_one)
        #cur.execute(query_two)
        create_contacts(cur)
        print_contacts(cur)
        #print("Table contacts has created successfully.")
        # Close Connection
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)