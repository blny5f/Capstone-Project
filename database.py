# database.py
import sqlite3
import requests
from bs4 import BeautifulSoup

def table_init():
    # store course information in Course_Info.db
    file = sqlite3.connect("Course_Info.db")
    cur = file.cursor()

    # initialize the entity 'COURSE' and each of its attributes
    # list of attributes is not finalized, will be updated as needed
    # Number refers to, for example, 1500 in Comp Sci 1500
    # Department is the official shortened name of the dept, e.g. CHEM ENG, ELEC ENG, etc., it should always fit in a varchar(8)
    # Available is a boolean that is true if it is being offered in the upcoming semester
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COURSE(
            Title VARCHAR(63) NOT NULL PRIMARY KEY,
            Department VARCHAR(8),
            Number INT, 
            Description VARCHAR(1023),
            numCredits FLOAT(1),
            Available BOOLEAN
            
        )
    """)

    # Recursive 'PREREQUISITE' relation, each row links a course to one of its prerequisites
    # if a course has multiple prerequisites, it will appear in multiple rows
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PREREQUISITE(
            courseTitle TEXT NOT NULL,
            prereqTitle TEXT NOT NULL,
            gradeReq VARCHAR(1)

        )
    """)
    
    file.commit()
    file.close()

