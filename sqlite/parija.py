import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
import sqlite3

# Connection to the database
conn = sqlite3.connect('epood_apeterson.db')
c = conn.cursor()

# Function to display data
def show_data():
    tree.delete(*tree.get_children())
    c.execute("SELECT * FROM apeterson")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# Function to search data
def search_data():
    search_term = search_entry.get()
    c.execute("SELECT * FROM apeterson WHERE  id LIKE ? OR first_name LIKE ? OR last_name LIKE ? OR email LIKE ? OR car_make LIKE ? OR car_model LIKE ? OR car_year LIKE ? OR car_price LIKE ?",
              ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
    rows = c.fetchall()
    if rows:
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    else:
        messagebox.showinfo("Search", "No data found")

# Function to add data
def add_data():
    eesnimi = eesnimi_entry.get()
    perekonnanimi = perekonnanimi_entry.get()
    email = email_entry.get()
    automark = automark_entry.get()
    automudel = automudel_entry.get()
    autoaasta = autoaasta_entry.get()
    autohind = autohind_entry.get()
    if eesnimi and perekonnanimi and email and automark and automudel and autoaasta and autohind:
        c.execute("INSERT INTO apeterson (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)", (eesnimi, perekonnanimi, email, automark, automudel, autoaasta, autohind))
        conn.commit()
        show_data()
        eesnimi_entry.delete(0, 'end')
        perekonnanimi_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        automark_entry.delete(0, 'end')
        automudel_entry.delete(0, 'end')
        autoaasta_entry.delete(0, 'end')
        autohind_entry.delete(0, 'end')
        messagebox.showinfo("Success", "Data added successfully")
    else:
        messagebox.showwarning("Warning", "Please fill in all fields")
# Function to delete data
def delete_data():
    selected_item = tree.selection()
    if selected_item:
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this?")
        if confirmation:
            for item in selected_item:
                c.execute("DELETE FROM apeterson WHERE rowid=?", (tree.item(item, "values")[0],))
                conn.commit()
            show_data()
    else:
        messagebox.showwarning("Warning", "Please select a row to delete")

# Tkinter application setup
root = tk.Tk()
root.title("Data Management")
root.geometry("1600x750")

# Ttkbootstrap theme style
style = Style(theme='darkly')  

# Displaying the data
tree = ttk.Treeview(root, columns=("ID", "Eesnimi", "Perekonnanimi", "Email", "Automark", "Automudel", "Autoaasta", "Autohind"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Eesnimi", text="Eesnimi")
tree.heading("Perekonnanimi", text="Perekonnanimi")
tree.heading("Email", text="Email")
tree.heading("Automark", text="Automark")
tree.heading("Automudel", text="Automudel")
tree.heading("Autoaasta", text="Autoaasta")
tree.heading("Autohind", text="Autohind")
tree.pack(pady=20)

# Additional option: Search functionality
search_label = ttk.Label(root, text="Search:")
search_label.pack()
search_entry = ttk.Entry(root, width=20)
search_entry.pack()
search_button = ttk.Button(root, text="Search", command=search_data)
search_button.pack()

# Additional option: Adding data
eesnimi_label = ttk.Label(root, text="Eesnimi:")
eesnimi_label.pack()
eesnimi_entry = ttk.Entry(root, width=20)
eesnimi_entry.pack()

perekonnanimi_label = ttk.Label(root, text="Perekonnanimi:")
perekonnanimi_label.pack()
perekonnanimi_entry = ttk.Entry(root, width=20)
perekonnanimi_entry.pack()

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root, width=20)
email_entry.pack()

automark_label = ttk.Label(root, text="Automark:")
automark_label.pack()
automark_entry = ttk.Entry(root, width=20)
automark_entry.pack()

automudel_label = ttk.Label(root, text="Automudel:")
automudel_label.pack()
automudel_entry = ttk.Entry(root, width=20)
automudel_entry.pack()

autoaasta_label = ttk.Label(root, text="Autoaasta:")
autoaasta_label.pack()
autoaasta_entry = ttk.Entry(root, width=20)
autoaasta_entry.pack()

autohind_label = ttk.Label(root, text="Autohind:")
autohind_label.pack()
autohind_entry = ttk.Entry(root, width=20)
autohind_entry.pack()

add_button = ttk.Button(root, text="Add Data", command=add_data)
add_button.pack()

# Additional option: Deleting data
delete_button = ttk.Button(root, text="Delete Selected", command=delete_data)
delete_button.pack()

# Displaying initial data
show_data()

# Running the application
root.mainloop()

# Closing the database connection