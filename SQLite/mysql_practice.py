import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",  # Change if you set different password
    database="school_db"
)

cursor = conn.cursor()

# CREATE DATABASE & TABLE
def setup_database():
    conn2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"
    )
    cursor2 = conn2.cursor()
    cursor2.execute("CREATE DATABASE IF NOT EXISTS school_db")
    conn2.close()
    print("✓ Database created")

# INSERT
def insert_student(name, email, age, grade):
    sql = "INSERT INTO students (name, email, age, grade) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, age, grade))
    conn.commit()
    print(f"✓ {name} added!")

# SELECT ALL
def get_all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- All Students ---")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

# UPDATE
def update_grade(student_id, grade):
    sql = "UPDATE students SET grade = %s WHERE id = %s"
    cursor.execute(sql, (grade, student_id))
    conn.commit()
    print(f"✓ Updated grade to {grade}")

# DELETE
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print(f"✓ Deleted student {student_id}")

# SEARCH
def search_by_grade(grade):
    sql = f"SELECT * FROM students WHERE grade = '{grade}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"\n--- Students with Grade {grade} ---")
    for student in result:
        print(f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}, Age: {student[3]}, Grade: {student[4]}")

# CREATE TABLE
def create_table():
    sql = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        age INT,
        grade VARCHAR(2)
    )
    """
    cursor.execute(sql)
    conn.commit()
    print("✓ Table created")

if __name__ == "__main__":
    setup_database()
    create_table()
    
    # Add students
    insert_student("Raj Kumar", "raj@test.com", 20, "A")
    insert_student("Priya Singh", "priya@test.com", 19, "B")
    insert_student("Amit Patel", "amit@test.com", 21, "A")
    
    # View all
    get_all_students()
    
    # Search by grade
    search_by_grade("A")
    
    # Update
    update_grade(1, "A+")
    
    # Delete
    delete_student(3)
    
    # Final list
    get_all_students()
    
    conn.close()
