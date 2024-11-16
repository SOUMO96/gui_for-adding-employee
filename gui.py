import tkinter as tk
from tkinter import messagebox

# Constants
MAX_EMPLOYEE = 100


# Employee structure as a class
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary


# Employee Manager class
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, id, salary):
        if len(self.employees) >= MAX_EMPLOYEE:
            messagebox.showwarning("Limit Reached", "Cannot add more employees.")
            return
        self.employees.append(Employee(name, id, salary))
        messagebox.showinfo("Success", "Employee added successfully.")

    def get_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None


# GUI Application class
class EmployeeApp:
    def __init__(self, root):
        self.manager = EmployeeManager()

        root.title("Employee Manager")
        root.geometry("300x300")

        # Add Employee section
        tk.Label(root, text="Add Employee").pack()

        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="ID:").pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        tk.Label(root, text="Salary:").pack()
        self.salary_entry = tk.Entry(root)
        self.salary_entry.pack()

        tk.Button(root, text="Add Employee", command=self.add_employee).pack()

        # Get Employee by ID section
        tk.Label(root, text="Get Employee by ID").pack()

        tk.Label(root, text="Search ID:").pack()
        self.search_id_entry = tk.Entry(root)
        self.search_id_entry.pack()

        tk.Button(root, text="Search", command=self.get_employee).pack()

    def add_employee(self):
        name = self.name_entry.get()
        try:
            id = int(self.id_entry.get())
            salary = int(self.salary_entry.get())
            self.manager.add_employee(name, id, salary)
        except ValueError:
            messagebox.showerror("Invalid Input", "ID and Salary must be integers.")
        self.clear_entries()

    def get_employee(self):
        try:
            search_id = int(self.search_id_entry.get())
            employee = self.manager.get_employee(search_id)
            if employee:
                messagebox.showinfo("Employee Found",
                                    f"Name: {employee.name}\nSalary: {employee.salary}\nID: {employee.id}")
            else:
                messagebox.showerror("Not Found", "Employee with given ID not found.")
        except ValueError:
            messagebox.showerror("Invalid Input", "ID must be an integer.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.search_id_entry.delete(0, tk.END)


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
