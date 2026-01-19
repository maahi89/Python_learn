import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

def run_custom_query():
    print("\n" + "=" * 50)
    print("INTERACTIVE SQL QUERY TESTER")
    print("=" * 50)
    print("\nExamples:")
    print("  SELECT * FROM students;")
    print("  SELECT name, age FROM students WHERE age > 20;")
    print("  SELECT COUNT(*) FROM students;")
    print("  Type 'quit' to exit\n")
    
    while True:
        query = input("Enter SQL query: ").strip()
        
        if query.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not query.endswith(';'):
            query += ';'
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            
            if results:
                print("\n📊 Results:")
                for row in results:
                    print(row)
            else:
                print("✓ Query executed successfully (no results)")
            print()
            
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    run_custom_query()
    conn.close()
