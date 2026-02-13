# 🎓 Student Management System

A complete **Python GUI application** with SQLite database and secure login authentication for managing student records.

---

## 📋 Features

### 🔐 Authentication System
- Secure login page
- Default credentials: `admin` / `1234`
- Session-based access control

### 👨‍🎓 Student Management
- ✅ **Add Student** - Insert new student records with auto-grade calculation
- 🔄 **Update Student** - Modify existing student information
- 🗑️ **Delete Student** - Remove student records with confirmation
- 🔍 **Search Student** - Find students by roll number
- 📊 **Show All** - Display all students in a table
- 📈 **Class Average** - Calculate average marks of all students
- 🏆 **Show Topper** - Display student with highest marks

### 💎 Professional Features
- ✔️ Input validation (roll number, marks range, empty fields)
- ✔️ Auto-grade calculation (A+, A, B+, B, C, D, F)
- ✔️ Confirmation dialogs before delete operations
- ✔️ Color-coded interface with modern design
- ✔️ Status bar with real-time feedback
- ✔️ Table with alternating row colors
- ✔️ Click table row to auto-fill fields
- ✔️ Logout functionality

---

## 📁 Project Structure

```
student_management_gui/
│
├── main.py          # Main application with GUI and logic
├── database.py      # Database operations and CRUD functions
├── students.db      # SQLite database (auto-created on first run)
└── README.md        # This file
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher (Tkinter and SQLite are built-in)

### Steps to Run

1. **Download/Clone the project**
   ```bash
   cd student_management_gui
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Login with default credentials**
   - Username: `admin`
   - Password: `1234`

That's it! The database will be created automatically on first run.

---

## 📖 How to Use

### 1️⃣ Login
- Enter username and password
- Click **LOGIN** or press **Enter**

### 2️⃣ Add Student
- Enter Roll No, Name, and Marks
- Click **➕ Add Student**
- Grade is automatically calculated

### 3️⃣ Update Student
- Enter Roll No with new Name/Marks
- Click **🔄 Update Student**
- Confirm the update

### 4️⃣ Delete Student
- Enter Roll No to delete
- Click **🗑 Delete Student**
- Confirm deletion

### 5️⃣ Search Student
- Enter Roll No
- Click **🔍 Search Student**
- Student details appear in table and fields

### 6️⃣ View Statistics
- **📊 Show All** - Display all students
- **📈 Class Average** - See average marks
- **🏆 Show Topper** - View top student

### 7️⃣ Quick Tips
- Click any table row to auto-fill fields
- Use **🔄 Clear Fields** to reset inputs
- Use **⎋ Logout** to return to login screen

---

## 🎨 Grade Calculation

| Marks Range | Grade |
|------------|-------|
| 90 - 100   | A+    |
| 80 - 89    | A     |
| 70 - 79    | B+    |
| 60 - 69    | B     |
| 50 - 59    | C     |
| 40 - 49    | D     |
| 0 - 39     | F     |

---

## 🔧 Technical Details

### Technologies Used
- **Python 3** - Programming language
- **Tkinter** - GUI framework (built-in)
- **SQLite3** - Database (built-in)
- **ttk** - Modern widgets

### Database Schema

**students table:**
```sql
CREATE TABLE students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks REAL NOT NULL,
    grade TEXT NOT NULL
)
```

**admin table:**
```sql
CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
```

---

## ✅ Input Validation

The system validates:
- ✔️ All fields must be filled
- ✔️ Roll number must be positive integer
- ✔️ Marks must be between 0-100
- ✔️ Duplicate roll numbers are prevented
- ✔️ Confirmation required before deletion

---

## 🎯 Testing Checklist

- [x] Valid login (admin/1234)
- [x] Invalid login credentials
- [x] Add student with valid data
- [x] Add student with duplicate roll number
- [x] Add student with empty fields
- [x] Add student with invalid marks (negative, >100)
- [x] Update existing student
- [x] Update non-existent student
- [x] Delete student with confirmation
- [x] Delete without selecting student
- [x] Search existing student
- [x] Search non-existent student
- [x] Calculate class average
- [x] Show topper
- [x] Logout functionality
- [x] Click table row to fill fields

---

## 📸 Screenshots

### Login Screen
- Clean and professional login interface
- Default credentials displayed
- Enter key support

### Main Dashboard
- Modern header with logout button
- Input fields for student data
- 8 action buttons with icons
- Interactive table with scrollbars
- Status bar for feedback

### Features Demo
- Add student with auto-grade calculation
- Update with confirmation dialog
- Delete with warning message
- Search with result highlighting
- Statistics (average and topper)

---

## 🎓 Project Information

**Project Name:** Student Management System  
**Language:** Python 3  
**Type:** Desktop GUI Application  
**Database:** SQLite  
**Frameworks:** Tkinter (GUI)

---

## 👨‍💻 Developer Notes

### Code Quality
- Clean, well-documented code
- Type hints for better readability
- Error handling throughout
- Modular design (separate database class)
- Follow Python best practices

### Future Enhancements (Optional)
- [ ] Password hashing (bcrypt/SHA-256)
- [ ] Export to CSV/Excel
- [ ] Print student report cards
- [ ] Bulk import from CSV
- [ ] Advanced search (by name, grade)
- [ ] Student photos
- [ ] Attendance tracking
- [ ] Dark/Light theme toggle

---

## 📝 License

This is an educational project. Free to use and modify for learning purposes.

---

## 🆘 Troubleshooting

**Problem:** Database not found  
**Solution:** The database is auto-created. Ensure write permissions in the folder.

**Problem:** Login not working  
**Solution:** Default credentials are `admin` / `1234`

**Problem:** Tkinter import error  
**Solution:** Tkinter is built-in with Python. Ensure Python is properly installed.

---

## 📞 Support

For questions or issues, please check:
1. This README file
2. Code comments in `main.py` and `database.py`
3. Python/Tkinter documentation

---

**Happy Coding! 🚀**
