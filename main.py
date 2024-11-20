# main.py
import database as db
import functions as func
import ui

def main():
  settings = None
  db.init()
  func.login()
  while True:
    func.menu(settings)


main()
