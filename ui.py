import tkinter as tk
import functions as fn
import sqlite3 as sq
import database as db
from courses import courses

current_profile_email = None
current_profile_sID = None
current_profile_fname = None
current_profile_lname = None

default_width = 1920
default_height = 1080

course_button_width = 60
back_button_width = 10

def show_course_list():
    for widget in window.winfo_children():
        widget.destroy()

    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=back_button_width, command=open_app)
    back_button.grid(row=0, column=0, pady=20, sticky="w")

    label = tk.Label(window, text="Course List", bg="white", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    scroll_frame = tk.Frame(window)
    scroll_frame.grid(row=2, column=0, sticky="nsew")

    window.grid_rowconfigure(2, weight=0)
    window.grid_columnconfigure(0, weight=0)

    canvas = tk.Canvas(scroll_frame)
    scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)

    course_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=course_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar.grid(row=0, column=1, sticky="ns")
    scroll_frame.grid_rowconfigure(0, weight=0)
    scroll_frame.grid_columnconfigure(0, weight=0)

    for index, (title, dep, num, description, num_credits, available) in enumerate(courses):
        row = index // 2
        col = index % 2
        course_code = f'CS {num}'
        course_code_title = f'{course_code} {title}'
        button = tk.Button(course_frame, text=course_code_title, font=("Arial", 12), bg="light grey", width=course_button_width, command=lambda msg=course_code: show_course_content(msg))
        button.grid(row=row+2, column=col, pady=5, padx=5, sticky="w")

    course_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"), width=1100, height=800)


def show_course_content(num):
    global current_course_num
    current_course_num = num

    for widget in window.winfo_children():
        widget.destroy()


    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=back_button_width, command=show_course_list)
    back_button.grid(row=0, column=0, pady=20, sticky="w")

    tk.Label(window, text=num, font=("Arial", 16), bg="white").grid(row=1, column=0, pady=20, sticky="w")

    syllabus_button = tk.Button(window, text="Syllabus/General Information", font=("Arial", 12), bg="light grey", width=25, command=lambda: show_info("Syllabus/General Information"))
    syllabus_button.grid(row=2, column=0, pady=5, sticky="w")

    example_button = tk.Button(window, text="Example Material", font=("Arial", 12), bg = "light grey", width=15, command=lambda: show_material("Example Material"))
    example_button.grid(row=3, column=0, pady=5, sticky="w")


def show_info(msg):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=back_button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def show_material(msg):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=back_button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def login_screen():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Login", font=("Arial", 16), bg="white").grid(row=0, column=0, sticky="sw")

    tk.Label(window, text="Email:", font=("Arial", 12), bg="white").grid(pady=(20,5), row=1, column=0, sticky="ne")
    email_entry = tk.Entry()
    email_entry.grid(row=1, column=1, sticky="sw", pady=(0,5))

    tk.Label(window, text="Password:", font=("Arial", 12), bg="white").grid(padx=(30,0),row=2, column=0, sticky="ne")
    password_entry = tk.Entry(show="*")
    password_entry.grid(row=2, column=1, sticky="ne",pady=(0,10))

    tk.Button(window, text="Log in", bg="light grey", command=lambda: login_credentials(email_entry, password_entry)).grid(pady=(20,0), row=4, column=1)
    create_acc_bttn = tk.Button(window, text="Create account", bg="light grey", command=create_account_screen)
    create_acc_bttn.grid(pady=(10,0),row=5, column=1)


def create_account_screen():
    for widget in window.winfo_children():
        widget.destroy()

    create_label = tk.Label(window, text="Create New Account", font=("Arial", 16), bg="white")
    create_label.grid(row=0, column=0, sticky="sw", columnspan=2)

    email_label = tk.Label(window, text="Email:", font=("Arial", 12), bg="white")
    email_label.grid(pady=(15,5), row=1, column=0, sticky="ne")

    email_entry = tk.Entry()
    email_entry.grid(row=1, column=1, sticky="sw", pady=(0,5))

    new_pass_label = tk.Label(window, text="New Password:", font=("Arial", 12), bg="white")
    new_pass_label.grid(padx=(30,0), row=2, column=0, sticky="ne")

    password_entry = tk.Entry(show="*")
    password_entry.grid(row=2, column=1, sticky="sw", pady=(0,5))

    conf_pass_label = tk.Label(window, text="Confirm Password:", font=("Arial", 12), bg="white")
    conf_pass_label.grid(row=3, column=0, sticky="ne")

    confirm_password_entry = tk.Entry(show="*")
    confirm_password_entry.grid(row=3, column=1, sticky="sw", pady=(0,5))

    sID_label = tk.Label(window, text="Student ID:", font=("Arial", 12), bg="white")
    sID_label.grid(row=4, column=0, sticky="ne")

    sID_entry = tk.Entry()
    sID_entry.grid(row=4, column=1, sticky="sw", pady=(0,5))

    fname_label = tk.Label(window, text="First Name:", font=("Arial", 12), bg="white")
    fname_label.grid(row=5, column=0, sticky="ne")

    fname_entry = tk.Entry()
    fname_entry.grid(row=5, column=1, sticky="sw", pady=(0,5))

    lname_label = tk.Label(window, text="Last Name:", font=("Arial", 12), bg="white")
    lname_label.grid(row=6, column=0, sticky="ne")

    lname_entry = tk.Entry()
    lname_entry.grid(row=6, column=1, sticky="sw", pady=(0,5))

    login_button = tk.Button(window, text="Log in", bg="light grey", command=lambda: check_password(email_entry.get(), password_entry.get(), confirm_password_entry.get(), sID_entry.get(), fname_entry.get(), lname_entry.get()))
    login_button.grid(pady=(10,0), row=7, column=1)

    back_button = tk.Button(window, text="Back", bg="light grey", command=login_screen)
    back_button.grid(pady=(5,0), row=9, column=1)


def check_password(email, password, conf_password, sID, fname, lname):
    if(password):
        if(password == conf_password):
            add_new_account(email, password, sID, fname, lname)
            login_screen()
        else:
            match_error_label = tk.Label(window, text="Error: Passwords do not match.", font=("Arial", 11), bg="white")
            match_error_label.grid(row=8, column=0, columnspan=2)
    else:
        error_label = tk.Label(window, text="Please enter a password.", font=("Arial", 11), bg="white")
        error_label.grid(row=8, column=0, columnspan=2)


def add_new_account(email, password, sID, fname, lname):
    file = sq.connect("Course_Info.db")
    cur = file.cursor()

    cur.execute("""
        INSERT INTO USER_PROFILE (Email, Password, studentID, firstName, lastName)
        VALUES (?, ?, ?, ?, ?)
    """, (email, password, sID, fname, lname))

    file.commit()
    file.close()


def get_profile_info(email):
    file = sq.connect("Course_Info.db", timeout=10)
    cur = file.cursor()

    cur.execute("""
        SELECT studentID, firstName, lastName
        FROM USER_PROFILE
        WHERE Email = ?""", (email,)
    )

    profile = cur.fetchone()
    file.close()

    return profile


def login_credentials(email_entry, password_entry):
    global current_profile_email, current_profile_sID, current_profile_fname, current_profile_lname

    email = email_entry.get()
    password = password_entry.get()
    if(fn.valid_login(email, password)):
        current_profile_email = email
        current_profile_sID, current_profile_fname, current_profile_lname = get_profile_info(email)
        open_app()
    else:
        invalid_label = tk.Label(window, text="Invalid email or password. Please try again", font=("Arial", 11), bg="white", wraplength=350)
        invalid_label.grid(row=3, column=0, columnspan=6, sticky="sw")


def show_profile_info():
    for widget in window.winfo_children():
        widget.destroy()

    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=back_button_width, command=open_app)
    back_button.grid(row=0, column=0, pady=(20,0), sticky="w")

    label = tk.Label(window, text="Student Profile", font=("Arial", 18), bg="white")
    label.grid(row=1, column=0, pady=20, sticky="w")

    name = f"Name: {current_profile_fname} {current_profile_lname}"
    name_label = tk.Label(window, text=name, font=("Arial", 12), bg="white")
    name_label.grid(row=2, column=0, pady=(0,3), sticky="w")

    email = f"Email: {current_profile_email}"
    email_label = tk.Label(window, text=email, font=("Arial", 12), bg="white")
    email_label.grid(row=3, column=0, pady=3, sticky="w")

    studentID = f"Student ID: {current_profile_sID}"
    ID_label = tk.Label(window, text=studentID, font=("Arial", 12), bg="white")
    ID_label.grid(row=4, column=0, pady=3, sticky="w")


def logout():
    global current_profile_email, current_profile_sID, current_profile_fname, current_profile_lname
    current_profile_email = None
    current_profile_sID = None
    current_profile_fname = None
    current_profile_lname = None
    login_screen()


def open_app():
    for widget in window.winfo_children():
        widget.destroy()

    welcome_msg = f"Welcome, {current_profile_fname}!"
    welcome_label = tk.Label(window, text=welcome_msg, font=("Arial", 16), bg="white")
    welcome_label.grid(row=0, column=0, pady=20, sticky="w")

    opt1_button = tk.Button(window, text="View Course List", font=("Arial", 12), bg="light grey", width=15, command=show_course_list)
    opt1_button.grid(row=1, column=0, pady=5, sticky="w")

    opt2_button = tk.Button(window, text="View Profile", font=("Arial", 12), bg="light grey", width=12, command=show_profile_info)
    opt2_button.grid(row=2, column=0, pady=5, sticky="w")

    logout_button = tk.Button(window, text="Log out", font=("Arial", 12), bg="light grey", width=7, command=logout)
    logout_button.grid(row=5, column=0, pady=10, sticky="w")


window = tk.Tk()
window.title("Course Catalog")
window.geometry(f"{default_width}x{default_height}")
window.configure(bg="white")
for i in range(50):
  window.grid_columnconfigure(i, minsize=16)
  window.grid_rowconfigure(i, minsize=16)

login_screen()

window.mainloop()
