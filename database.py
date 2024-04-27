import sqlite3
import pandas as pd

def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   status TEXT)''' )
    conn.commit()
    conn.close()

def add_gmail_column():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    # Check if the column already exists
    cursor.execute("PRAGMA table_info(Employees)")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    if 'gmail' not in column_names:
        # Add the column if it doesn't exist
        cursor.execute('ALTER TABLE Employees ADD COLUMN gmail VARCHAR(255)')
        conn.commit()
    conn.close()


def add_age_and_department_columns():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Employees)")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    if 'age' not in column_names:
        cursor.execute('ALTER TABLE Employees ADD COLUMN age INTEGER')
    if 'department' not in column_names:
        cursor.execute('ALTER TABLE Employees ADD COLUMN department TEXT')
    conn.commit()
    conn.close()





conn = sqlite3.connect('Employees.db')
with open('database_dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)
conn.close()




def fetch_employees():
    conn=sqlite3.connect('Employees.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees=cursor.fetchall()
    conn.close()
    return employees

def insert_employee(id, name, role, gender,gmail, status,age, department):
    conn=sqlite3.connect('Employees.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO Employees(id, name, role, gender, gmail, status,age, department) VALUES (?, ?, ?, ?, ?, ?,?,?)', (id, name, role, gender, gmail, status,age,department))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id=?', (id,))
    conn.commit()
    conn.close()

def update_employee(new_name, new_role,new_gender, new_gmail,new_age, new_department,new_status, id):
    conn=sqlite3.connect('Employees.db')
    cursor=conn.cursor()
    cursor.execute("UPDATE Employees SET name = ?, role = ?, gender =?, age = ?, department =?, gmail = ?, status = ? WHERE id = ?",
                   (new_name, new_role, new_gender, new_gmail, new_age, new_department,new_status, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn=sqlite3.connect('Employees.db')
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id=?', (id,))
    result=cursor.fetchone()
    conn.close()
    return result[0]>0




def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def store_data_in_excel():
    employees_data = fetch_employees()
    df = pd.DataFrame(employees_data, columns=['id', 'name', 'role', 'gender', 'status', 'gmail', 'age', 'department'])
    df.to_excel('employees_data.xlsx', index=False)



add_age_and_department_columns()
add_gmail_column()
create_table()
store_data_in_excel()
