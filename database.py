"""
Database Module for Student Management System
Handles all database operations including student CRUD and authentication
"""

import sqlite3
from typing import Optional, List, Tuple

class Database:
    """Handles all database operations for the Student Management System"""
    
    def __init__(self, db_name: str = "students.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_name = db_name
        self.create_tables()
        self.create_default_admin()
    
    def get_connection(self):
        """Create and return a database connection"""
        return sqlite3.connect(self.db_name)
    
    def create_tables(self):
        """Create students and admin tables if they don't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create students table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                marks REAL NOT NULL,
                grade TEXT NOT NULL
            )
        """)
        
        # Create admin table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        
        conn.commit()
        conn.close()
    
    def create_default_admin(self):
        """Create default admin account (admin/1234) if it doesn't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO admin (username, password) VALUES (?, ?)",
                ("admin", "1234")
            )
            conn.commit()
        except sqlite3.IntegrityError:
            # Admin already exists
            pass
        finally:
            conn.close()
    
    # ==================== AUTHENTICATION ====================
    
    def verify_login(self, username: str, password: str) -> bool:
        """
        Verify admin login credentials
        Returns True if credentials are valid, False otherwise
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM admin WHERE username = ? AND password = ?",
            (username, password)
        )
        
        result = cursor.fetchone()
        conn.close()
        
        return result is not None
    
    # ==================== STUDENT CRUD OPERATIONS ====================
    
    def calculate_grade(self, marks: float) -> str:
        """Calculate grade based on marks"""
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B+"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
    
    def add_student(self, roll_no: int, name: str, marks: float) -> Tuple[bool, str]:
        """
        Add a new student to the database
        Returns (success: bool, message: str)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            grade = self.calculate_grade(marks)
            cursor.execute(
                "INSERT INTO students (roll_no, name, marks, grade) VALUES (?, ?, ?, ?)",
                (roll_no, name, marks, grade)
            )
            conn.commit()
            conn.close()
            return (True, "Student added successfully!")
        except sqlite3.IntegrityError:
            conn.close()
            return (False, f"Roll number {roll_no} already exists!")
        except Exception as e:
            conn.close()
            return (False, f"Error: {str(e)}")
    
    def update_student(self, roll_no: int, name: str, marks: float) -> Tuple[bool, str]:
        """
        Update existing student record
        Returns (success: bool, message: str)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            grade = self.calculate_grade(marks)
            cursor.execute(
                "UPDATE students SET name = ?, marks = ?, grade = ? WHERE roll_no = ?",
                (name, marks, grade, roll_no)
            )
            
            if cursor.rowcount == 0:
                conn.close()
                return (False, f"Roll number {roll_no} not found!")
            
            conn.commit()
            conn.close()
            return (True, "Student updated successfully!")
        except Exception as e:
            conn.close()
            return (False, f"Error: {str(e)}")
    
    def delete_student(self, roll_no: int) -> Tuple[bool, str]:
        """
        Delete student by roll number
        Returns (success: bool, message: str)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
            
            if cursor.rowcount == 0:
                conn.close()
                return (False, f"Roll number {roll_no} not found!")
            
            conn.commit()
            conn.close()
            return (True, "Student deleted successfully!")
        except Exception as e:
            conn.close()
            return (False, f"Error: {str(e)}")
    
    def search_student(self, roll_no: int) -> Optional[Tuple]:
        """
        Search for student by roll number
        Returns student data tuple or None if not found
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
        result = cursor.fetchone()
        conn.close()
        
        return result
    
    def get_all_students(self) -> List[Tuple]:
        """
        Get all students from database
        Returns list of student tuples
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM students ORDER BY roll_no")
        results = cursor.fetchall()
        conn.close()
        
        return results
    
    def get_class_average(self) -> Optional[float]:
        """
        Calculate and return class average marks
        Returns average marks or None if no students
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT AVG(marks) FROM students")
        result = cursor.fetchone()
        conn.close()
        
        return result[0] if result[0] is not None else None
    
    def get_topper(self) -> Optional[Tuple]:
        """
        Get the student with highest marks
        Returns student data tuple or None if no students
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        
        return result
    
    def student_exists(self, roll_no: int) -> bool:
        """Check if student with given roll number exists"""
        return self.search_student(roll_no) is not None