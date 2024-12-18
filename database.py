# database.py
import sqlite3 as sq
import os
from bs4 import BeautifulSoup
from courses import courses

# initialize the entity 'COURSE' and each of its attributes
# list of attributes is not finalized, will be updated as needed
# Number refers to, for example, 1500 in Comp Sci 1500
# Department is the official shortened name of the dept, e.g. CHEM ENG, ELEC ENG, etc., it should always fit in a varchar(8)
# Available is a boolean that is true if it is being offered in the upcoming semester and has open seats
def init():
  # store course information in Course_Info.db
  file = sq.connect("Course_Info.db")
  cur = file.cursor()
  cur.execute("""
    CREATE TABLE IF NOT EXISTS COURSE(
      Title VARCHAR(63) NOT NULL PRIMARY KEY,
      Department VARCHAR(8),
      Number INT,
      Description TEXT,
      numCredits FLOAT(1),
      Available BOOLEAN
    )
  """);

  # Recursive 'REQUIRES' relation, each row links a course to one of its prerequisites
  # if a course has multiple prerequisites, it will appear in multiple rows
  cur.execute("""
    CREATE TABLE IF NOT EXISTS REQUIRES(
      courseTitle VARCHAR(63) NOT NULL,
      prereqTitle VARCHAR(63) NOT NULL,
      gradeReq VARCHAR(1)
    )
  """);

  # 'ENROLLED' relation, each row contains a studentID and the title of one of the courses in which they are enrolled
  cur.execute("""
    CREATE TABLE IF NOT EXISTS ENROLLED(
      studentID VARCHAR(8) NOT NULL,
      courseTitle VARCHAR(63) NOT NULL
    )
  """);

  # 'COMPLETED' relation, each row contains a studentID, the title of a course which they have completed, and their final grade
  cur.execute("""
    CREATE TABLE IF NOT EXISTS COMPLETED(
      studentID VARCHAR(8) NOT NULL,
      courseTitle VARCHAR(63) NOT NULL,
      grade VARCHAR(1) NOT NULL
    )
  """);

  # 'USER_PROFILE' entity, used to store information specific to each student
  # user will log in using email and password
  cur.execute("""
    CREATE TABLE IF NOT EXISTS USER_PROFILE(
      studentID VARCHAR(8) NOT NULL PRIMARY KEY,
      firstName VARCHAR(24),
      lastName VARCHAR(24),
      Password VARCHAR(24) NOT NULL,
      Email VARCHAR(31) NOT NULL
    )
  """);

  # 'ATTENDS' relation, each row contains a studentID and the classID of a class they attend
  cur.execute("""
    CREATE TABLE IF NOT EXISTS ATTENDS(
      studentID VARCHAR(8) NOT NULL,
      classID VARCHAR(8) NOT NULL
    )
  """);

  # 'CLASS' entity, stores information about the classes being held for each course
  # classType attribute distinguishes lecture/lab/recitation
  cur.execute("""
    CREATE TABLE IF NOT EXISTS CLASS(
      classID VARCHAR(8) NOT NULL PRIMARY KEY,
      courseDept VARCHAR(8) NOT NULL,
      courseNum INT,
      classType VARCHAR(12),
      Instructor VARCHAR(48),
      sectionNum INT,
      seatsOpen INT,
      daysHeld TEXT,
      Location TEXT,
      timeHeld TIME
    )
  """);

  # 'OFFERS' relation, links the courses to each of their respective classes
  cur.execute("""
    CREATE TABLE IF NOT EXISTS OFFERS(
      courseTitle VARCHAR(63) NOT NULL,
      classID VARCHAR(8) NOT NULL
    )
  """);

  for course in courses:
    cur.execute("""
      REPLACE INTO COURSE(Title, Department, Number, Description, numCredits, Available)
        VALUES (?, ?, ?, ?, ?, ?)
    """, course);

  for user in users:
    cur.execute("""
      REPLACE INTO USER_PROFILE(studentID, firstName, lastName, Email, Password)
        VALUES (?, ?, ?, ?, ?)
    """, user);

  file.commit()
  file.close()
