import sqlite3

# Create/connect to database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# CLEAR TABLE (reset data)
def clear_all_students():
    cursor.execute("DELETE FROM students")
    conn.commit()
    print("🗑️  Database cleared!")

# INSERT DATA
def insert_student(name, email, age, grade):
    cursor.execute("INSERT INTO students (name, email, age, grade) VALUES (?, ?, ?, ?)",
                   (name, email, age, grade))
    conn.commit()
    print(f"✓ Student {name} added!")

# SELECT DATA
def get_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- All Students ---")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

# UPDATE DATA
def update_student(student_id, grade):
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (grade, student_id))
    conn.commit()
    print(f"✓ Student {student_id} updated to grade {grade}")

# DELETE DATA
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"✓ Student {student_id} deleted")

# SEARCH DATA
def search_student(name):
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    result = cursor.fetchall()
    print(f"\n--- Search Results for '{name}' ---")
    for student in result:
        print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

if __name__ == "__main__":
    # Clear old data first
    clear_all_students()
    
    # Add some students
    insert_student("Raj Kumar", "raj@example.com", 20, "A")
    insert_student("Priya Singh", "priya@example.com", 19, "B")
    insert_student("Amit Patel", "amit@example.com", 21, "A")

    # Get all students
    get_all_students()
    
    # Search
    search_student("Raj")
    
    # Update
    update_student(1, "A+")
    
    # Get updated list
    get_all_students()
    
    conn.close()
