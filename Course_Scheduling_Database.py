# Course_Scheduling_Database.py
import sqlite3

def table_init():
    # store course information in Course_Info.db
    file = sqlite3.connect("Course_Info.db")
    cur = file.cursor()

    # initialize the entity 'Course' and each of its attributes
    # list of attributes is not finalized, will be updated as needed
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Course(
            COURSE_TITLE varchar(63),
            COURSE_CODE varchar(15), 
            COURSE_DESCRIPTION varchar(1023),
            CREDIT_HOURS float(1),
            PREREQUISITE_CODES varchar(15),
            
            




        )
    """)