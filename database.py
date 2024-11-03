# database.py
import sqlite3
import os
from bs4 import BeautifulSoup

def init():
  # store course information in Course_Info.db
  file = sqlite3.connect("Course_Info.db")
  cur = file.cursor()
  # initialize the entity 'COURSE' and each of its attributes
  # list of attributes is not finalized, will be updated as needed
  # Number refers to, for example, 1500 in Comp Sci 1500
  # Department is the official shortened name of the dept, e.g. CHEM ENG, ELEC ENG, etc., it should always fit in a varchar(8)
  # Available is a boolean that is true if it is being offered in the upcoming semester and has open seats
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
      Email VARCHAR(31) NOT NULL,
      Standing VARCHAR(10)
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

  # TEMPORARY TEST DATA
  cur.execute("""
    REPLACE INTO COURSE(Title, Department, Number, Description, numCredits, Available) VALUES
      ('Python', 'Comp Sci', 1500, 'We teach python here', 3, 1),
      ('C++', 'Comp Sci', 1575, 'We teach c++ here', 3, 1),
      ('Boolean Algebra', 'Comp Sci', 2200, 'We teach boolean algebra here', 3, 1),
      ('Java', 'Comp Sci', 2400, 'We teach java here', 3, 0),
      ('Data Structures', 'Comp Sci', 2500, 'We teach data structures here', 3, 1),
      ('Web Development', 'Comp Sci', 2600, 'We teach web development here', 3, 1),
      ('Machine Learning', 'Comp Sci', 2700, 'We teach machine learning here', 3, 1),
      ('Operating Systems', 'Comp Sci', 2800, 'We teach operating systems here', 3, 0),
      ('Database Systems', 'Comp Sci', 2900, 'We teach database systems here', 3, 1),
      ('Network Security', 'Comp Sci', 3000, 'We teach network security here', 3, 1),
      ('Artificial Intelligence', 'Comp Sci', 3100, 'We teach artificial intelligence here', 3, 0),
      ('Software Engineering', 'Comp Sci', 3200, 'We teach software engineering here', 3, 1);
      ('Computer Graphics', 'Comp Sci', 3300, 'We teach computer graphics here', 3, 1),
      ('Mobile App Development', 'Comp Sci', 3400, 'We teach mobile app development here', 3, 1),
      ('Human-Computer Interaction', 'Comp Sci', 3500, 'We teach human-computer interaction here', 3, 1),
      ('Cloud Computing', 'Comp Sci', 3600, 'We teach cloud computing here', 3, 0),
      ('Cybersecurity', 'Comp Sci', 3700, 'We teach cybersecurity here', 3, 1),
      ('Game Development', 'Comp Sci', 3800, 'We teach game development here', 3, 1),
      ('Big Data Analytics', 'Comp Sci', 3900, 'We teach big data analytics here', 3, 1),
      ('Software Testing', 'Comp Sci', 4000, 'We teach software testing here', 3, 1);
  """);

  cur.execute("""
    REPLACE INTO USER_PROFILE(studentID, firstName, lastName, Password, Email, Standing) VALUES
      ('1', 'James', 'Sullivan', 'password123', 'jss4kh@mst.edu', 'Senior'),
      ('2', 'Mike', 'Wazowski', 'pass12345', 'msw123@mst.edu', 'Senior'),
      ('3', 'Samantha', 'Williams', 'securePass456', 'saw789@mst.edu', 'Junior'),
      ('4', 'Oliver', 'Johnson', 'myPassword1', 'ojh456@mst.edu', 'Sophomore'),
      ('5', 'Emily', 'Davis', 'passw0rd!', 'edw123@mst.edu', 'Freshman'),
      ('6', 'Daniel', 'Brown', 'password2024', 'dab000@mst.edu', 'Senior'),
      ('7', 'Sophia', 'Garcia', 'qwerty123', 'sgarcia@mst.edu', 'Junior'),
      ('8', 'Liam', 'Martinez', 'letmein123', 'lmartinez@mst.edu', 'Senior'),
      ('9', 'Mia', 'Rodriguez', 'abc123456', 'mrodriguez@mst.edu', 'Sophomore'),
      ('10', 'Noah', 'Hernandez', 'iloveyou!', 'nh@mst.edu', 'Freshman');
      ('11', 'Ava', 'Martinez', 'password111', 'avmartinez@mst.edu', 'Sophomore'),
      ('12', 'Ethan', 'Lopez', 'secret1234', 'el@mst.edu', 'Freshman'),
      ('13', 'Isabella', 'Gonzalez', 'mypassword1', 'igonzalez@mst.edu', 'Junior'),
      ('14', 'Lucas', 'Wilson', 'abc1234567', 'lwilson@mst.edu', 'Senior'),
      ('15', 'Charlotte', 'Anderson', 'letmeinagain!', 'canderson@mst.edu', 'Senior'),
      ('16', 'James', 'Thomas', 'password!@#', 'jthomas@mst.edu', 'Junior'),
      ('17', 'Mason', 'Taylor', 'qwertyuiop', 'mtaylor@mst.edu', 'Sophomore'),
      ('18', 'Ella', 'Moore', 'passwordpass', 'emoore@mst.edu', 'Freshman');
  """);

  file.commit()
  file.close()
