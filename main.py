"""
Student Management System - Main Application
A complete GUI application with MODERN MINIMAL UI, login authentication and student management features
"""

import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class LoginWindow:
    """Login window for authentication"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management System - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Initialize database
        self.db = Database()
        
        # Configure modern minimal colors
        self.bg_color = "#f4f6f8"
        self.fg_color = "#111827"
        self.button_color = "#2563eb"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create login form widgets"""
        # Title
        title_label = tk.Label(
            self.root,
            text="🎓 Student Management System",
            font=("Segoe UI", 18, "bold"),
            bg=self.bg_color,
            fg="#1e293b"
        )
        title_label.pack(pady=30)
        
        # Frame for login form
        login_frame = tk.Frame(self.root, bg=self.bg_color)
        login_frame.pack(pady=20)
        
        # Username
        tk.Label(
            login_frame,
            text="Username:",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg="#374151"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.username_entry = tk.Entry(
            login_frame,
            font=("Segoe UI", 11),
            width=20,
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb"
        )
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.username_entry.focus()
        
        # Password
        tk.Label(
            login_frame,
            text="Password:",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg="#374151"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.password_entry = tk.Entry(
            login_frame,
            font=("Segoe UI", 11),
            width=20,
            show="*",
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb"
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Login button with modern styling
        login_btn = tk.Button(
            self.root,
            text="LOGIN",
            font=("Segoe UI", 11, "bold"),
            bg=self.button_color,
            fg="white",
            width=15,
            cursor="hand2",
            bd=0,
            padx=15,
            pady=10,
            relief=tk.FLAT,
            command=self.login
        )
        login_btn.pack(pady=20)
        
        # Hover effect
        login_btn.bind("<Enter>", lambda e: login_btn.config(bg="#1d4ed8"))
        login_btn.bind("<Leave>", lambda e: login_btn.config(bg=self.button_color))
        
        # Info label
        info_label = tk.Label(
            self.root,
            text="Default: admin / 1234",
            font=("Segoe UI", 9, "italic"),
            bg=self.bg_color,
            fg="#6b7280"
        )
        info_label.pack()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.login())
    
    def login(self):
        """Handle login button click"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password!")
            return
        
        if self.db.verify_login(username, password):
            self.root.destroy()
            # Open main application
            app = StudentManagementApp()
            app.run()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()
    
    def run(self):
        """Start the login window"""
        self.root.mainloop()


class StudentManagementApp:
    """Main Student Management Application with MODERN MINIMAL UI"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management System - Dashboard")
        self.root.geometry("1000x600")
        
        # Initialize database
        self.db = Database()
        
        # Configure modern minimal colors
        self.bg_color = "#f4f6f8"
        self.header_color = "#1e293b"
        self.button_color = "#2563eb"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
        self.load_all_students()
    
    def create_modern_button(self, parent, text, command, bg_color):
        """Create a modern flat button with hover effect"""
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=bg_color,
            fg="white",
            activebackground=bg_color,
            activeforeground="white",
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
            command=command,
            relief=tk.FLAT
        )
        
        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg=self.darken_color(bg_color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        
        return btn
    
    def darken_color(self, color):
        """Darken a hex color by reducing RGB values"""
        color = color.lstrip('#')
        r = int(color[0:2], 16) - 20
        g = int(color[2:4], 16) - 20
        b = int(color[4:6], 16) - 20
        
        r = max(0, r)
        g = max(0, g)
        b = max(0, b)
        
        return f'#{r:02x}{g:02x}{b:02x}'
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # ==================== HEADER ====================
        header_frame = tk.Frame(self.root, bg=self.header_color, height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="🎓 STUDENT MANAGEMENT SYSTEM",
            font=("Segoe UI", 18, "bold"),
            bg=self.header_color,
            fg="white"
        ).pack(side=tk.LEFT, padx=20, pady=10)
        
        # Logout button with modern style
        logout_btn = tk.Button(
            header_frame,
            text="⎋ Logout",
            font=("Segoe UI", 10, "bold"),
            bg="#dc2626",
            fg="white",
            cursor="hand2",
            bd=0,
            padx=15,
            pady=8,
            relief=tk.FLAT,
            command=self.logout
        )
        logout_btn.pack(side=tk.RIGHT, padx=20)
        
        # Hover effect for logout button
        logout_btn.bind("<Enter>", lambda e: logout_btn.config(bg="#b91c1c"))
        logout_btn.bind("<Leave>", lambda e: logout_btn.config(bg="#dc2626"))
        
        # ==================== INPUT FRAME ====================
        input_frame = tk.LabelFrame(
            self.root,
            text="  Student Information  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg="#111827",
            padx=20,
            pady=15,
            bd=0,
            relief=tk.FLAT
        )
        input_frame.pack(padx=20, pady=20, fill=tk.X)
        
        # Roll Number
        tk.Label(
            input_frame,
            text="Roll No:",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg="#374151"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="e")
        
        self.roll_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 10),
            width=20,
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb"
        )
        self.roll_entry.grid(row=0, column=1, padx=10, pady=8)
        
        # Name
        tk.Label(
            input_frame,
            text="Name:",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg="#374151"
        ).grid(row=0, column=2, padx=10, pady=8, sticky="e")
        
        self.name_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 10),
            width=25,
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb"
        )
        self.name_entry.grid(row=0, column=3, padx=10, pady=8)
        
        # Marks
        tk.Label(
            input_frame,
            text="Marks:",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg="#374151"
        ).grid(row=0, column=4, padx=10, pady=8, sticky="e")
        
        self.marks_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 10),
            width=15,
            bd=1,
            relief=tk.SOLID,
            highlightthickness=1,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb"
        )
        self.marks_entry.grid(row=0, column=5, padx=10, pady=8)
        
        # ==================== BUTTON FRAME ====================
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=15)
        
        # Define modern minimal buttons with clean colors
        buttons = [
            ("Add", self.add_student, "#2563eb"),
            ("Update", self.update_student, "#16a34a"),
            ("Delete", self.delete_student, "#dc2626"),
            ("Search", self.search_student, "#7c3aed"),
            ("Show All", self.load_all_students, "#0ea5e9"),
            ("Average", self.show_average, "#f59e0b"),
            ("Topper", self.show_topper, "#14b8a6"),
            ("Clear", self.clear_fields, "#6b7280")
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = self.create_modern_button(button_frame, text, command, color)
            btn.config(width=12)
            btn.grid(row=i//4, column=i%4, padx=12, pady=12)
        
        # ==================== TABLE FRAME ====================
        table_frame = tk.LabelFrame(
            self.root,
            text="  Student Records  ",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg_color,
            fg="#111827",
            padx=10,
            pady=10,
            bd=0,
            relief=tk.FLAT
        )
        table_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Configure modern ttk style for Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="#111827",
                        rowheight=30,
                        fieldbackground="white",
                        font=("Segoe UI", 10),
                        borderwidth=0)
        style.configure("Treeview.Heading",
                        font=("Segoe UI", 11, "bold"),
                        background="#f9fafb",
                        foreground="#111827",
                        borderwidth=1,
                        relief=tk.FLAT)
        style.map("Treeview.Heading",
                  background=[("active", "#e5e7eb")])
        style.map("Treeview",
                  background=[("selected", "#2563eb")],
                  foreground=[("selected", "white")])
        
        # Scrollbar
        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        
        # Treeview
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("Roll No", "Name", "Marks", "Grade"),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
            height=10
        )
        
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        scroll_y.config(command=self.student_table.yview)
        scroll_x.config(command=self.student_table.xview)
        
        # Configure columns
        self.student_table.heading("Roll No", text="Roll No")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Marks", text="Marks")
        self.student_table.heading("Grade", text="Grade")
        
        self.student_table["show"] = "headings"
        
        self.student_table.column("Roll No", width=100, anchor=tk.CENTER)
        self.student_table.column("Name", width=250, anchor=tk.W)
        self.student_table.column("Marks", width=100, anchor=tk.CENTER)
        self.student_table.column("Grade", width=100, anchor=tk.CENTER)
        
        self.student_table.pack(fill=tk.BOTH, expand=True)
        
        # Configure row colors with modern palette
        self.student_table.tag_configure('oddrow', background='#ffffff')
        self.student_table.tag_configure('evenrow', background='#f9fafb')
        
        # Bind row selection
        self.student_table.bind('<ButtonRelease-1>', self.get_cursor)
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            font=("Segoe UI", 9),
            bg=self.header_color,
            fg="white",
            anchor=tk.W,
            relief=tk.FLAT,
            padx=10
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def validate_inputs(self):
        """Validate user inputs"""
        roll_no = self.roll_entry.get().strip()
        name = self.name_entry.get().strip()
        marks = self.marks_entry.get().strip()
        
        if not roll_no or not name or not marks:
            messagebox.showerror("Error", "All fields are required!")
            return None
        
        try:
            roll_no = int(roll_no)
            if roll_no <= 0:
                messagebox.showerror("Error", "Roll number must be positive!")
                return None
        except ValueError:
            messagebox.showerror("Error", "Roll number must be a valid integer!")
            return None
        
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                messagebox.showerror("Error", "Marks must be between 0 and 100!")
                return None
        except ValueError:
            messagebox.showerror("Error", "Marks must be a valid number!")
            return None
        
        return (roll_no, name, marks)
    
    def add_student(self):
        """Add new student to database"""
        data = self.validate_inputs()
        if data is None:
            return
        
        roll_no, name, marks = data
        success, message = self.db.add_student(roll_no, name, marks)
        
        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
            self.load_all_students()
            self.status_bar.config(text=f"Student {name} added successfully")
        else:
            messagebox.showerror("Error", message)
    
    def update_student(self):
        """Update existing student record"""
        data = self.validate_inputs()
        if data is None:
            return
        
        roll_no, name, marks = data
        
        # Confirm update
        confirm = messagebox.askyesno(
            "Confirm Update",
            f"Do you want to update student with Roll No: {roll_no}?"
        )
        
        if not confirm:
            return
        
        success, message = self.db.update_student(roll_no, name, marks)
        
        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
            self.load_all_students()
            self.status_bar.config(text=f"Student {name} updated successfully")
        else:
            messagebox.showerror("Error", message)
    
    def delete_student(self):
        """Delete student from database"""
        roll_no = self.roll_entry.get().strip()
        
        if not roll_no:
            messagebox.showerror("Error", "Please enter Roll Number to delete!")
            return
        
        try:
            roll_no = int(roll_no)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll Number!")
            return
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete student with Roll No: {roll_no}?\n\nThis action cannot be undone!"
        )
        
        if not confirm:
            return
        
        success, message = self.db.delete_student(roll_no)
        
        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
            self.load_all_students()
            self.status_bar.config(text=f"Student with Roll No {roll_no} deleted")
        else:
            messagebox.showerror("Error", message)
    
    def search_student(self):
        """Search for student by roll number"""
        roll_no = self.roll_entry.get().strip()
        
        if not roll_no:
            messagebox.showerror("Error", "Please enter Roll Number to search!")
            return
        
        try:
            roll_no = int(roll_no)
        except ValueError:
            messagebox.showerror("Error", "Invalid Roll Number!")
            return
        
        result = self.db.search_student(roll_no)
        
        if result:
            # Clear table and show only searched student
            self.student_table.delete(*self.student_table.get_children())
            self.student_table.insert('', tk.END, values=result, tags=('oddrow',))
            
            # Fill entry fields with student data
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, result[1])
            self.marks_entry.delete(0, tk.END)
            self.marks_entry.insert(0, result[2])
            
            self.status_bar.config(text=f"Found student: {result[1]}")
        else:
            messagebox.showinfo("Not Found", f"No student found with Roll No: {roll_no}")
            self.status_bar.config(text=f"Student with Roll No {roll_no} not found")
    
    def load_all_students(self):
        """Load and display all students in table"""
        self.student_table.delete(*self.student_table.get_children())
        
        students = self.db.get_all_students()
        
        for i, student in enumerate(students):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.student_table.insert('', tk.END, values=student, tags=(tag,))
        
        total = len(students)
        self.status_bar.config(text=f"Total Students: {total}")
    
    def show_average(self):
        """Calculate and display class average"""
        average = self.db.get_class_average()
        
        if average is not None:
            messagebox.showinfo(
                "Class Average",
                f"📊 Class Average Marks: {average:.2f}%"
            )
            self.status_bar.config(text=f"Class average: {average:.2f}%")
        else:
            messagebox.showinfo("No Data", "No students in database!")
    
    def show_topper(self):
        """Find and display class topper"""
        topper = self.db.get_topper()
        
        if topper:
            roll_no, name, marks, grade = topper
            
            # Highlight topper in table
            self.student_table.delete(*self.student_table.get_children())
            self.student_table.insert('', tk.END, values=topper, tags=('oddrow',))
            
            messagebox.showinfo(
                "Class Topper 🏆",
                f"Topper Details:\n\n"
                f"Roll No: {roll_no}\n"
                f"Name: {name}\n"
                f"Marks: {marks}\n"
                f"Grade: {grade}"
            )
            
            self.status_bar.config(text=f"Class Topper: {name} ({marks} marks)")
        else:
            messagebox.showinfo("No Data", "No students in database!")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        self.roll_entry.focus()
        self.status_bar.config(text="Fields cleared")
    
    def get_cursor(self, event):
        """Get data from selected row in table"""
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        
        if row:
            self.roll_entry.delete(0, tk.END)
            self.roll_entry.insert(0, row[0])
            
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, row[1])
            
            self.marks_entry.delete(0, tk.END)
            self.marks_entry.insert(0, row[2])
    
    def logout(self):
        """Logout and return to login screen"""
        confirm = messagebox.askyesno(
            "Confirm Logout",
            "Are you sure you want to logout?"
        )
        
        if confirm:
            self.root.destroy()
            login = LoginWindow()
            login.run()
    
    def run(self):
        """Start the main application"""
        self.root.mainloop()


# ==================== MAIN ENTRY POINT ====================

if __name__ == "__main__":
    # Start with login window
    login = LoginWindow()
    login.run()