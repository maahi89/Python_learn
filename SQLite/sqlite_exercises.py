import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

print("=" * 50)
print("SQL PRACTICE EXERCISES")
print("=" * 50)

# EXERCISE 1: Display all students
print("\n1️⃣ EXERCISE 1: Get All Students")
print("-" * 50)
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()
for student in all_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

# EXERCISE 2: Count total students
print("\n2️⃣ EXERCISE 2: Count Total Students")
print("-" * 50)
cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]
print(f"Total Students: {total}")

# EXERCISE 3: Get students with grade 'A'
print("\n3️⃣ EXERCISE 3: Students with Grade A")
print("-" * 50)
cursor.execute("SELECT * FROM students WHERE grade = 'A'")
grade_a_students = cursor.fetchall()
for student in grade_a_students:
    print(f"{student[1]} - Grade: {student[4]}")

# EXERCISE 4: Get average age
print("\n4️⃣ EXERCISE 4: Average Age of Students")
print("-" * 50)
cursor.execute("SELECT AVG(age) FROM students")
avg_age = cursor.fetchone()[0]
print(f"Average Age: {avg_age:.2f} years")

# EXERCISE 5: Get oldest student
print("\n5️⃣ EXERCISE 5: Oldest Student")
print("-" * 50)
cursor.execute("SELECT * FROM students ORDER BY age DESC LIMIT 1")
oldest = cursor.fetchone()
print(f"Oldest: {oldest[1]} - Age: {oldest[3]}")

# EXERCISE 6: Get youngest student
print("\n6️⃣ EXERCISE 6: Youngest Student")
print("-" * 50)
cursor.execute("SELECT * FROM students ORDER BY age ASC LIMIT 1")
youngest = cursor.fetchone()
print(f"Youngest: {youngest[1]} - Age: {youngest[3]}")

# EXERCISE 7: Sort by name
print("\n7️⃣ EXERCISE 7: Students Sorted by Name")
print("-" * 50)
cursor.execute("SELECT * FROM students ORDER BY name ASC")
for student in cursor.fetchall():
    print(f"{student[1]} ({student[3]} years old)")

# EXERCISE 8: Count students by grade
print("\n8️⃣ EXERCISE 8: Students Count by Grade")
print("-" * 50)
cursor.execute("SELECT grade, COUNT(*) as count FROM students GROUP BY grade")
for row in cursor.fetchall():
    print(f"Grade {row[0]}: {row[1]} students")

# EXERCISE 9: Students above age 20
print("\n9️⃣ EXERCISE 9: Students Above Age 20")
print("-" * 50)
cursor.execute("SELECT * FROM students WHERE age > 20")
for student in cursor.fetchall():
    print(f"{student[1]} - Age: {student[3]}")

# EXERCISE 10: Update multiple grades
print("\n🔟 EXERCISE 10: Update All 'B' Grades to 'B+'")
print("-" * 50)
cursor.execute("UPDATE students SET grade = 'B+' WHERE grade = 'B'")
conn.commit()
print("✓ Updated successfully!")

cursor.execute("SELECT * FROM students WHERE grade = 'B+'")
for student in cursor.fetchall():
    print(f"{student[1]} - New Grade: {student[4]}")

print("\n" + "=" * 50)
print("All exercises completed!")
print("=" * 50)

conn.close()
