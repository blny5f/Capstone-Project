# functions.py
import sqlite3 as sq

# display function, takes SQL fetch data as parameter
def display(results):
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


# sort function for course list search results
def sort(results):
  file = sq.connect("Course_Info.db")
  cur = file.cursor()

  while True:
    try:
      print("\n1. Title\n2. Department\n3. Number\n4. Credits\n5. Availability")
      option = int(input("\nSort by? "))
      if option in {1, 2, 3, 4, 5}:
        break
      else:
        print("Please select a valid option.")
    except ValueError:
      print("Please select a valid option.")


  if option != 5:
    results = sorted(results, key = lambda course: course[option-1])
  else:
    results = sorted(results, key = lambda course: course[option-1], reverse = True)

  display(results)
  return results

# filter settings function
def filter_settings(settings):
  # default settings values, stored in 'settings' tuple
  if settings is None:
    num_bool = False
    avail_bool = True
    num_lower_bound = 0
    num_upper_bound = 9999
    settings = (num_bool, num_lower_bound, num_upper_bound, avail_bool)

  while True:
    try:
      print("\n1. Number\n2. Change number bounds\n3. Availability\n4. Return to main menu")
      option = int(input("\nSelect a setting to change it. "))
      if option in {1, 2, 3, 4}:
        break
      else:
        print("Please select a valid option.")
    except ValueError:
      print("Please select a valid option.")

  match(option):
    case 1:
      num_bool = not num_bool
      if(num_bool):
        print("Number filter has been turned ON.")
      else:
        print("Number filter has been turned OFF.")
    case 2:
      while True:
        try:
          num_lower_bound = int(input("Enter lower bound: "))
          num_upper_bound = int(input("Enter upper bound: "))
          break
        except ValueError:
          print("Please enter a valid number")
    case 3:
      avail_bool = not avail_bool
      if(avail_bool):
        print("Available filter has been turned ON.")
      else:
        print("Available filter has been turned OFF.")
    case 4:
      return settings


# filter function for search results
def results_filter(results):
  file = sq.connect("Course_Info.db")
  cur = file.cursor()

  while True:
    try:
      print("\n1. Number\n2. Credits\n3. Available")
      option = int(input("\nFilter by? "))
      if option in {1, 2, 3}:
        break
      else:
        print("Please select a valid option.")
    except ValueError:
      print("Please select a valid option.")

  results = list(filter(lambda course: course[option + 1], results))
  display(results)

  return results


# search function for course list
def search():
  file = sq.connect("Course_Info.db")
  cur = file.cursor()

  # take string to search as input and select matches, sorted by ascending course number
  search_term = input("Search: ")
  print("\nSearching...")
  cur.execute("""
    SELECT Title, Department, Number, numCredits, Available
    FROM Course
    WHERE Title LIKE ? OR Department LIKE ? OR Number LIKE ?
    ORDER BY Number ASC
  """, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))

  # fetch results and print the number of results found
  results = cur.fetchall()
  display(results)

  # give user options after displaying results
  # loop until valid choice is given
  while True:
    try:
      print("\n1. Sort results\n2. Apply filters\n3. Search again\n4. Return to main menu")
      option = int(input("\nEnter a number to select an option: "))
      if option in {1, 2, 3, 4}:
        break
      else:
        print("Please select a valid option.")
    except ValueError:
      print("Please select a valid option.")

  match(option):
    case 1:
      sort(results)
    case 2:
      results_filter(results)
    case 3:
      search()
    case 4:
      return


# check if login credentials are valid
def valid_login(email, password):
  # connect to database and find a match for the given login information
  file = sq.connect("Course_Info.db")
  cur = file.cursor()
  cur.execute("""SELECT Email, Password
    FROM User_Profile
    WHERE Email = ?
    AND Password = ?""", (email, password)
  )

  # if no results from fetchone(), invalid login information, try again
  # otherwise, greet user with their first name
  profile = cur.fetchone()
  file.close()
  if profile is None:
    return 0
  else:
    return 1


# menu function, called after logging in
def menu(settings):
  # display options
  print("\n1: Search the course list\n2: Filter settings\n3: Exit the program")

  # loop until user enters valid number
  while True:
    try:
      option = int(input("\nEnter a number to select an option: "))
      if option in {1, 2, 3}:
        break
      else:
        print("Please select a valid option.")
    except ValueError:
      print("Please enter a valid number.")

  # match inputted integer with corresponding option function
  match option:
    case 1:
      search()
    case 2:
      filter_settings(settings)
    case 3:
      exit()


# new account creation, adds new user to database
def new_account():
  new_email = input("University Email: ")
  new_password = input("New Password: ")
  confirm_new_password = input("Confirm New Password: ")
  if(new_password != confirm_new_password):
    new_password = ''
    confirm_new_password = ''
    print("Passwords do not match. Please try again.")
  else:
    print("Account created.")

