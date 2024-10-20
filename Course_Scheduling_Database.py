# Course_Scheduling_Database.py
import sqlite3

def table_init():
    # store course information in Course_Info.db
    file = sqlite3.connect("Course_Info.db")
    cur = file.cursor()

    # initialize the entity 'COURSE' and each of its attributes
    # list of attributes is not finalized, will be updated as needed
    # NUMBER refers to, for example, 1500 in Comp Sci 1500
    # DEPARTMENT is the official shortened name of the dept, e.g. CHEM ENG, ELEC ENG, etc., it should always fit in a varchar(8)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COURSE(
            TITLE varchar(63) NOT NULL PRIMARY KEY,
            DEPARTMENT varchar(8),
            NUMBER int, 
            DESCRIPTION varchar(1023),
            NUM_CREDITS float(1)
            
        )
    """)

    # Recursive 'PREREQUISITE' relation, each row links a course to one of its prerequisites
    # if a course has multiple prerequisites, it will appear in multiple rows
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PREREQUISITE(
            TITLE varchar(63),
            PREREQUISITE_TITLE varchar(63)

        )
    """)