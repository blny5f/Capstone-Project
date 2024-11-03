# main.py
import database as db
import functions as func

def main():
	db.init()
	while True:
		func.menu()


main()
