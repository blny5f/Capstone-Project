# functions.py
import sqlite3 as sq

def search():
  file = sq.connect("Course_Info.db")
  cur = file.cursor()

  search_term = input("Search: ")
  cur.execute("""SELECT Title, Department, Number, numCredits, Available
    FROM Course
    WHERE Title LIKE ?
    """, ('%' + search_term + '%',))

  results = cur.fetchall()
  print(f'\n{len(results)} Results\n')

  col1 = 'TITLE'
  col2 = 'DEPARTMENT'
  col3 = 'NUMBER'
  col4 = 'CREDITS'
  col5 = 'AVAILABILITY'
  col_gap = 30
  num_divs = 142

  print(f'{col1:<{col_gap}} {col2:<{col_gap}} {col3:<{col_gap}} {col4:<{col_gap}} {col5:<{col_gap}}')
  print('-' * num_divs)

  for course in results:
    if(course[4] == 1):
      avail = 'AVAILABLE'
    else:
      avail = 'NOT AVAILABLE'

    print(f'{course[0]:<{col_gap}} {course[1]:<{col_gap}} {course[2]:<{col_gap}} {course[3]:<{col_gap}} {avail:<{col_gap}}')

  print('-' * num_divs)


def menu():
  print("\n1: Search the course list\n2: option 2\n3: Exit the program")

  # loop until user enters valid number
  while True:
    try:
      option = int(input("\nEnter a number to select an option: "))
      break

    except ValueError:
      print("Please enter a valid number.")

  match option:
    case 1:
      search()
    case 2:
      print("option 2")
    case 3:
      exit()
