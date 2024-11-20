import tkinter as tk
import functions as fn

current_course_num = None

default_width = 1024
default_height = 768

button_width = 20

def show_course_list():
    for widget in window.winfo_children():
        widget.destroy()


    tk.Label(window, text="Course Selection", font=("Arial", 16), bg="white").pack(pady=10, anchor="w")

    courses = [
    	("Python", "CS-1500"),
    	("C++", "CS-1575"),
    	("Boolean Algebra", "CS-2200"),
    	("Java", "CS-2400"),
    	("Data Structures", "CS-2500"),
    	("Web Development", "CS-2600"),
    	("Machine Learning", "CS-2700"),
    	("Operating Systems", "CS-2800"),
    	("Database Systems", "CS-2900"),
    	("Network Security", "CS-3000"),
    	("Artificial Intelligence", "CS-3100"),
    	("Software Engineering", "CS-3200"),
    	("Computer Graphics", "CS-3300"),
    	("Mobile App Development", "CS-3400"),
    	("Human-Computer Interaction", "CS-3500"),
    	("Cloud Computing", "CS-3600"),
    	("Cybersecurity", "CS-3700"),
    	("Game Development", "CS-3800"),
    	("Big Data Analysis", "CS-3900"),
    	("Software Testing", "CS-4000")
	]

    course_frame = tk.Frame(window, bg="white")
    course_frame.pack(pady=10, anchor="w")

    for index, (course_name, course_num) in enumerate(courses):
        row = index % 10
        col = index // 10
        button = tk.Button(course_frame, text=course_name, font=("Arial", 12), bg="light grey", width=button_width, command=lambda msg=course_num: show_course_content(msg))
        button.grid(row=row, column=col, pady=5, padx=5, sticky="w")

    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=open_app)
    back_button.pack(pady=20, anchor="w")


def show_course_content(num):
    global current_course_num
    current_course_num = num

    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=num, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")

    syllabus_button = tk.Button(window, text="Syllabus/General Information", font=("Arial", 12), bg="light grey", width=button_width, command=lambda: show_info("Syllabus/General Information"))
    syllabus_button.pack(pady=5, anchor="w")

    example_button = tk.Button(window, text="Example Material", font=("Arial", 12), bg = "light grey", width=button_width, command=lambda: show_material("Example Material"))
    example_button.pack(pady=5, anchor="w")

    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def show_info(msg):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def show_material(msg):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def login_screen():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Login", font=("Arial", 16), bg="white").grid(row=0, column=0, sticky="sw")
    tk.Label(window, text="Email:", font=("Arial", 12), bg="white").grid(pady=(20,0),row=1, column=0, sticky="ne")
    email_entry = tk.Entry()
    email_entry.grid(row=1, column=1, sticky="sw")
    tk.Label(window, text="Password:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="ne")
    password_entry = tk.Entry()
    password_entry.grid(row=2, column=1, sticky="ne",pady=(0,10))
    tk.Button(window, text="Log in", bg="light grey", command=lambda: login_credentials(email_entry, password_entry)).grid(pady=(20,0), row=4, column=1)
    create_acc_bttn = tk.Button(window, text="Create account", bg="light grey", command=create_account_screen)
    create_acc_bttn.grid(pady=(10,0),row=5, column=1)


def create_account_screen():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Create New Account", font=("Arial", 16), bg="white").grid(row=0, column=0, sticky="sw", columnspan=2)
    tk.Label(window, text="Email:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="se")
    email_entry = tk.Entry()
    email_entry.grid(row=1, column=1, sticky="sw")
    tk.Label(window, text="New Password:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="se")
    password_entry = tk.Entry()
    password_entry.grid(row=2, column=1, sticky="sw")
    tk.Button(window, text="Log in", bg="light grey", command=open_app).grid(row=3, column=1)
    back_button = tk.Button(window, text="Back", bg="light grey", command=login_screen)
    back_button.grid(row=5, column=1, sticky="nw")


def login_credentials(email_entry, password_entry):
    email = email_entry.get()
    password = password_entry.get()
    if(fn.valid_login(email, password)):
        open_app()
    else:
        invalid_label = tk.Label(window, text="Invalid email or password. Please try again", font=("Arial", 12), bg="white", wraplength=350)
        invalid_label.grid(row=3, column=0, columnspan=6, sticky="sw")


def open_app():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Choose Your Degree Path", font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    cs_button = tk.Button(window, text="Computer Science", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    cs_button.pack(pady=10, anchor="w")


window = tk.Tk()
window.title("Capstone I")
window.geometry(f"{default_width}x{default_height}")
window.configure(bg="white")
for i in range(50):
  window.grid_columnconfigure(i, minsize=16)
  window.grid_rowconfigure(i, minsize=16)


login_screen()

window.mainloop()
