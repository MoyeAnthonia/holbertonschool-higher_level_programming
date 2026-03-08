#!/usr/bin/python3
"""List all states from the database hbtn_0e_usa"""

import sys
import MySQLdb


def main():
    """Get arguments: username, password, database"""
    user = sys.argv[1]
    passwrd = sys.argv[2]
    database = sys.argv[3]
    argument = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwrd,
        db=database
    )


    cur = db.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE BINARY name LIKE '{}%' "
                "ORDER BY id ASC".format(argument))

 
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()