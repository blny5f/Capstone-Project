# functions.py
import sqlite3 as sq

# search function for course list
def search():
  file = sq.connect("Course_Info.db")
  cur = file.cursor()

  # take string to search as input and select matches
  search_term = input("Search: ")
  print("\nSearching...")
  cur.execute("""SELECT Title, Department, Number, numCredits, Available
    FROM Course
    WHERE Title LIKE ?
    """, ('%' + search_term + '%',))

  # fetch results and print the number of results found
  results = cur.fetchall()
  print(f'\n{len(results)} Results\n')

  # basic UI to format results cleanly
  col1 = 'TITLE'
  col2 = 'DEPARTMENT'
  col3 = 'NUMBER'
  col4 = 'CREDITS'
  col5 = 'AVAILABILITY'
  col_gap = 30
  num_divs = 142

  # print headers of each column
  print(f'{col1:<{col_gap}} {col2:<{col_gap}} {col3:<{col_gap}} {col4:<{col_gap}} {col5:<{col_gap}}')
  print('-' * num_divs)


  # recursively print each result
  # convert 'Available' boolean in course[4] to a readable format
  for course in results:
    if(course[4] == 1):
      avail = 'AVAILABLE'
    else:
      avail = 'NOT AVAILABLE'

    print(f'{course[0]:<{col_gap}} {course[1]:<{col_gap}} {course[2]:<{col_gap}} {course[3]:<{col_gap}} {avail:<{col_gap}}')

  print('-' * num_divs)


# login function to call as website is opened
def login():
  # take email and password as input
  print('-' * 142)
  print("Login with your university Email and password.")
  email = input("Email: ")
  password = input("Password: ")

  # connect to database and find a match for the given login information
  print('-' * 142)
  file = sq.connect("Course_Info.db")
  cur = file.cursor()
  cur.execute("""SELECT Email, Password, firstName
    FROM User_Profile
    WHERE Email LIKE ?
    AND Password LIKE ?""", (email, password)
  )

  # if no results from fetchone(), invalid login information, try again
  # otherwise, greet user with their first name
  profile = cur.fetchone()
  if profile is None:
    print("Invalid Email or password.")
    login()
  else:
    print(f'Welcome, {profile[2]}!')


# menu function, called after logging in
def menu():
  # display options
  print("\n1: Search the course list\n2: option 2\n3: Exit the program")

  # loop until user enters valid number
  while True:
    try:
      option = int(input("\nEnter a number to select an option: "))
      break
    except ValueError:
      print("Please enter a valid number.")

  # match inputted integer with corresponding option function
  match option:
    case 1:
      search()
    case 2:
      print("option 2")
    case 3:
      exit()
