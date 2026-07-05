# 📚 Library Management System

A modern **Library Management System** built with **Python, Flask, and SQLite** that streamlines library operations through efficient book, member, and transaction management.

This project demonstrates full-stack development fundamentals, including CRUD operations, relational databases, backend validation, and a responsive web application architecture.

---

## ✨ Features

### 📖 Book Management
- Add new books
- View complete book collection
- Edit book details
- Delete books
- Search books instantly
- Low stock alerts
- Export book records to CSV
- Duplicate book validation

### 👥 Member Management
- Register new members
- View member records
- Edit member information
- Delete members
- Search members
- Email uniqueness validation
- Phone number validation

### 🔄 Book Issue & Return
- Issue books to registered members
- Return issued books
- Automatic inventory updates
- Prevent duplicate issue records
- Display only available books while issuing

### 📅 Loan Tracking
- Automatic issue date generation
- Automatic due date calculation
- Return date tracking
- Overdue status detection

### 📜 Transaction History
- Complete borrowing history
- Search by member or book
- Filter by loan status
- Track issued, returned, and overdue books

### 📊 Dashboard
- Total books
- Total members
- Issued books
- Available copies
- Low stock books
- Overdue books
- Recently added books

### 🛡️ Validations
- Prevent duplicate books
- Prevent duplicate member emails
- Prevent invalid phone numbers
- Prevent negative quantities
- Prevent deleting issued books
- Prevent deleting members with active loans
- Flash notifications for all actions

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Flask | Web Framework |
| SQLite | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Jinja2 | Templating Engine |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
Library-Management-System/
│
├── app.py
├── database.py
├── library.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── books.html
│   ├── members.html
│   ├── issue_book.html
│   ├── return_book.html
│   ├── history.html
│   ├── edit_book.html
│   └── edit_member.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── .gitignore
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/library-management-system.git
```

### 2. Navigate into the project

```bash
cd library-management-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🗄️ Database Schema

The project uses **SQLite** with the following tables:

### Books

- Book ID
- Title
- Author
- Category
- Quantity

### Members

- Member ID
- Name
- Email
- Phone

### Issued Books

- Issue ID
- Book ID
- Member ID
- Issue Date
- Due Date
- Return Date

---

# 📸 Screenshots

> UI redesign is currently in progress.

Future screenshots will include:

- Dashboard
- Books Module
- Members Module
- Issue Book
- Return Book
- Transaction History

---

# 🚀 Future Improvements

- Modern responsive UI
- Glassmorphism design
- Animated dashboard
- Dark mode enhancements
- Book cover uploads
- Authentication system
- PDF reports
- Charts & analytics
- Email reminders
- Cloud deployment

---

# 📚 Learning Outcomes

Through this project, I strengthened my understanding of:

- Flask application development
- SQLite database design
- CRUD operations
- SQL queries and joins
- Backend validation
- Jinja templating
- Form handling
- Business logic implementation
- Git and GitHub workflows

---

# 👩‍💻 Author

**Vanshika Sharma**

- GitHub: https://github.com/your-username
- LinkedIn: https://linkedin.com/in/your-linkedin

---

## ⭐ If you found this project interesting, consider giving it a star!
