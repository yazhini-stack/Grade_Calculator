import sqlite3
from tkinter import *

# connect database
conn = sqlite3.connect("grade.db")
cursor = conn.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
student_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
maths INTEGER,
science INTEGER,
english INTEGER
)
""")

conn.commit()


# function to calculate grade
def calculate():
    name = name_entry.get()
    maths = int(maths_entry.get())
    science = int(science_entry.get())
    english = int(english_entry.get())

    total = maths + science + english
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "FAIL"

    # insert into database
    cursor.execute(
        "INSERT INTO student(name, maths, science, english) VALUES(?,?,?,?)",
        (name, maths, science, english)
    )
    conn.commit()

    result_label.config(
        text=f"Total: {total}   Average: {average:.2f}   Grade: {grade}"
    )


# GUI window
root = Tk()
root.title("Grade Calculator")

Label(root, text="Student Name").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Maths Marks").grid(row=1, column=0)
maths_entry = Entry(root)
maths_entry.grid(row=1, column=1)

Label(root, text="Science Marks").grid(row=2, column=0)
science_entry = Entry(root)
science_entry.grid(row=2, column=1)

Label(root, text="English Marks").grid(row=3, column=0)
english_entry = Entry(root)
english_entry.grid(row=3, column=1)

Button(root, text="Calculate Grade", command=calculate).grid(row=4, column=1)

result_label = Label(root, text="")
result_label.grid(row=5, column=1)

root.mainloop()