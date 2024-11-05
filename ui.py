import tkinter as tk

current_course_num = None

restore_width = 300
restore_height = 400

zoom_width = 1800
zoom_height = 800

button_width = 20

def zoom_window():
	window.geometry(f"{zoom_width}x{zoom_height}")

def restore_window():
	window.geometry(f"{restore_width}x{restore_height}")

def create_control_frame():
	control_frame = tk.Frame(window, bg="white")
	control_frame.pack(pady=5, anchor="w")
	tk.Button(control_frame, text="Expand", bg="light grey", command=zoom_window).pack(side="left", padx=5)
	tk.Button(control_frame, text="Restore", bg="light grey", command=restore_window).pack(side="left", padx=5)
	return control_frame

def show_course_list():
    for widget in window.winfo_children():
        widget.destroy()

    create_control_frame()

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

    create_control_frame()
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

    create_control_frame()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")

def show_material(msg):
    for widget in window.winfo_children():
        widget.destroy()

    create_control_frame()

    tk.Label(window, text=msg, font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    back_button = tk.Button(window, text="Back", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    back_button.pack(pady=10, anchor="w")


def open_app():
    for widget in window.winfo_children():
        widget.destroy()

    create_control_frame()

    tk.Label(window, text="Choose Your Degree Path", font=("Arial", 16), bg="white").pack(pady=20, anchor="w")
    cs_button = tk.Button(window, text="Computer Science", font=("Arial", 12), bg="light grey", width=button_width, command=show_course_list)
    cs_button.pack(pady=10, anchor="w")

window = tk.Tk()
window.title("Capstone I")
window.geometry(f"{restore_width}x{restore_height}")
window.configure(bg="white")

open_app()

window.mainloop()
