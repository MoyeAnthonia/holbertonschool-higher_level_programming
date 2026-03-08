#!/usr/bin/python3
"""List all states from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


def main():
    """Set up the SQL Query"""
    user = sys.argv[1]
    passwrd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=passwrd,
        db=database
    )

    cur = db.cursor()


    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY id ASC"
                )


    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()