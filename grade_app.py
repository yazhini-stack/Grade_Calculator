import streamlit as st
import sqlite3
import pandas as pd

# Page setup
st.set_page_config(
    page_title="Student Grade Calculator",
    layout="centered"
)

# Database connection
conn = sqlite3.connect("grade.db")
cursor = conn.cursor()

# Drop old table (prevents column mismatch error)
cursor.execute("DROP TABLE IF EXISTS student")

# Create new table structure
cursor.execute("""
CREATE TABLE student(
reg_no TEXT PRIMARY KEY,
name TEXT,
probability INTEGER,
daa INTEGER,
dbms INTEGER,
se INTEGER,
aiml INTEGER,
os INTEGER,
total INTEGER,
average REAL,
grade TEXT
)
""")

conn.commit()


# Grade calculation function
def calculate_grade(avg):

    if avg >= 90:
        return "O"
    elif avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B+"
    elif avg >= 50:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


# Title
st.title("🎓 Student Grade Calculator")


# Student details input
reg_no = st.text_input("Enter Register Number")
name = st.text_input("Enter Student Name")

st.subheader("Enter Subject Marks")

probability = st.number_input("Probability & Statistics", 0, 100)
daa = st.number_input("DAA", 0, 100)
dbms = st.number_input("DBMS", 0, 100)
se = st.number_input("Software Engineering", 0, 100)
aiml = st.number_input("AIML", 0, 100)
os = st.number_input("Operating Systems", 0, 100)


# Calculate result button
if st.button("Calculate Result"):

    total = probability + daa + dbms + se + aiml + os
    average = total / 6

    grade = calculate_grade(average)

    cursor.execute("""
    INSERT OR REPLACE INTO student
    VALUES(?,?,?,?,?,?,?,?,?,?,?)
    """,
    (reg_no, name, probability, daa, dbms, se, aiml, os, total, average, grade)
    )

    conn.commit()

    st.success(f"Total Marks = {total}")
    st.success(f"Average = {average:.2f}")

    st.markdown(f"## 🎯 Final Grade: {grade}")


# Show records button
if st.button("Show Student Records"):

    cursor.execute("SELECT * FROM student")

    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=[
        "Register No",
        "Name",
        "Probability",
        "DAA",
        "DBMS",
        "SE",
        "AIML",
        "OS",
        "Total",
        "Average",
        "Grade"
    ])

    st.subheader("📊 Stored Student Records")

    st.dataframe(df)