import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app=customtkinter.CTk()
app.title('Employee Management System')
app.geometry('1350x700')
app.config(bg='#ececec')
app.resizable(False,False)

font1=('Goudy Old Style',20,'bold')
font2=('Goudy Old Style',17,'bold')


def add_to_treeview():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    role_entry.delete(0,END)
    variable1.set('MALE')
    variable2.set('IT')
    age_entry.delete(0,END)
    gmail_entry.delete(0,END)
    status_entry.delete(0,END)

def display_data(event):
    selected_item=tree.focus()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        role_entry.insert(0,row[2])
        variable1.set(row[3])
        gmail_entry.insert(0,row[4])
        status_entry.insert(0,row[5])
        age_entry.insert(0,row[6])
        variable2.set(row[7])
    else:
        pass
        
def update():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an Employee to Update!')
    else:
        id=id_entry.get()
        name=name_entry.get()
        role=role_entry.get()
        gender=variable1.get()
        gmail=gmail_entry.get()
        department=variable2.get()
        age=age_entry.get()
        status=status_entry.get()
        database.update_employee(name,role, gender,status,gmail, id,age,department)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Succesfully Updated!')

def delete():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an Employee to Delete!')
    else:
        id=id_entry.get()
        database.delete_employee( id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted!')


def insert():
    id=id_entry.get()
    name=name_entry.get()
    role=role_entry.get()
    gender=variable1.get()
    gmail=gmail_entry.get()
    department=variable2.get()
    age=age_entry.get()
    status=status_entry.get()
    if not(id and  name and role and gender and gmail and status and age and department):
        messagebox.showerror('Error','Enter all Fields.')
    elif database.id_exists(id):
        messagebox.showerror('Error','ID Already exists.')
    else:
        database.insert_employee(id, name, role, gender, gmail, status, age, department)
        add_to_treeview()
        messagebox.showinfo('Success', 'Data has been inserted.')

        

id_label=customtkinter.CTkLabel(app,font=font1,text='ID' ,text_color='black',bg_color='#ececec',height=7)
id_label.place(x=20,y=20)

id_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180,height=7)
id_entry.place(x=130,y=20)

name_label=customtkinter.CTkLabel(app,font=font1,text='Name' ,text_color='black',bg_color='#ececec',height=7)
name_label.place(x=20,y=80)

name_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180,height=7)
name_entry.place(x=130,y=80)

role_label=customtkinter.CTkLabel(app,font=font1,text='Role' ,text_color='black',bg_color='#ececec')
role_label.place(x=20,y=140)

role_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180)
role_entry.place(x=130,y=140)

gender_label=customtkinter.CTkLabel(app,font=font1,text='Gender' ,text_color='black',bg_color='#ececec')
gender_label.place(x=20,y=200)

options=['Male', 'Female'] 
variable1=StringVar()

gender_options=customtkinter.CTkComboBox(app,font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#333333', button_color='#333333',button_hover_color='#ececec',border_color='#333333',width=180,variable=variable1,values=options,state='readonly')
gender_options.set('Male')
gender_options.place(x=130,y=200)


gmail_label=customtkinter.CTkLabel(app,font=font1,text='Gmail' ,text_color='black',bg_color='#ececec')
gmail_label.place(x=20,y=260)

gmail_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180)
gmail_entry.place(x=130,y=260)

status_label=customtkinter.CTkLabel(app,font=font1,text='Status' ,text_color='black',bg_color='#ececec')
status_label.place(x=20,y=320)

status_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180)
status_entry.place(x=130,y=320)

age_label=customtkinter.CTkLabel(app,font=font1,text='Age' ,text_color='black',bg_color='#ececec')
age_label.place(x=20,y=380)

age_entry=customtkinter.CTkEntry(app,font=font1 ,text_color='#fff',bg_color='#0C9295',border_width=2,width=180)
age_entry.place(x=130,y=380)

department_label=customtkinter.CTkLabel(app,font=font1,text='Department' ,text_color='black',bg_color='#ececec')
department_label.place(x=20,y=430)

options=['IT', 'NON-IT','Others'] 
variable2=StringVar()

department_options=customtkinter.CTkComboBox(app,font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#333333', button_color='#333333',button_hover_color='#0C9295',border_color='#333333',width=180,variable=variable2,values=options,state='readonly')
department_options.set('IT')
department_options.place(x=130,y=430)



add_button=customtkinter.CTkButton(app,command=insert,font=font1, text_color="#fff", text='Add Employee',fg_color='#161C25',hover_color="#00850B",cursor='hand2',corner_radius=5,border_width=2,width=258)
add_button.place(x=40,y=500)

clear_button=customtkinter.CTkButton(app,command=lambda:clear(True),font=font1, text_color="#fff", text='New Employee',fg_color='#161C25', bg_color="#ececec", border_width=2,cursor='hand2',corner_radius=5,width=260)
clear_button.place(x=40,y=540)

update_button=customtkinter.CTkButton(app,command=update,font=font1, text_color="#fff", text='Update Employee',fg_color='#161C25', bg_color="#ececec", border_width=2,cursor='hand2',corner_radius=5,width=260)
update_button.place(x=40,y=580)

delete_button=customtkinter.CTkButton(app,command=delete,font=font1, text_color="#fff", text='Delete Employee',fg_color='#161C25',hover_color="#AE0000", bg_color="#ececec", border_width=2,cursor='hand2',corner_radius=5,width=260)
delete_button.place(x=40,y=620)



style=ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=("Abadi", 14),foreground='#fff',background='#000',fieldbackground='#545454',height=50)
style.map('Treeview',background=[('selected','#579514')])

tree=ttk.Treeview(app,height=50)

tree['columns']=('ID','Name','Role','Gender','Status','Gmail','Age','Department')

tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',anchor=tk.CENTER,width=120)
tree.column('Name',anchor=tk.CENTER,width=350)
tree.column('Role',anchor=tk.CENTER,width=200)
tree.column('Gender',anchor=tk.CENTER,width=200)
tree.column('Status',anchor=tk.CENTER,width=200)
tree.column('Gmail',anchor=tk.CENTER,width=200)
tree.column('Age',anchor=tk.CENTER,width=200)
tree.column('Department',anchor=tk.CENTER,width=200)


tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Status',text='Status')
tree.heading('Gmail',text='Gmail')
tree.heading('Age',text='Age')
tree.heading('Department',text='Department')


tree.place(x=600,y=30)


tree.bind('<ButtonRelease>', display_data)
add_to_treeview()
app.mainloop()






