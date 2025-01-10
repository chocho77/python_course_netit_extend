import mysql.connector

charsets = [None, 'latin1', 'utf8mb3', 'utf8mb4', 'utf8']
for cs in charsets:
    print('-------------------------------------------------------------------------')
    print('attempting connect with charset ' + str(cs))
    dbconn=None
    try:
        if cs is None:
            dbconn = mysql.connector.connect(user='root', password='xQNM#2@yKL'
                , database='companny', host='localhost', port=3306)
        elif cs == 'utf8mb3':
            dbconn = mysql.connector.connect(user='root', password='xQNM#2@yKL'
                , database='companny', host='localhost', port=3306, charset=cs, collation='utf8mb3_general_ci')
        else:
            dbconn = mysql.connector.connect(user='root', password='xQNM#2@yKL'
                , database='companny', host='localhost', port=3306, charset=cs)
    except mysql.connector.Error as err:
        print('ERROR: {}'.format(err))
    if not dbconn is None:
        dbconn.close()
