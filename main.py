# main.py
import database as db
import functions as func

def main():
  db.init()
  func.login()
  while True:
    func.menu()


main()
