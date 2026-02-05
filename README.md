# 📚 Bookstore Django Project

This is a Django-based web application built for learning and sharing. It includes two apps:

- `book_outlet`: Displays and manages book listings.
- `registration`: Handles user registration and form submissions.

Feel free to clone, explore, and build on top of it!

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Kishan06319/Bookstore.git
cd Bookstore
```

### 2. Create a Virtual Environment
```bash
python -m venv env
```

### 3. Activate the Environment
- On **Windows**:
```bash
env\Scripts\activate
```
- On **macOS/Linux**:
```bash
source env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist yet, you can generate it with:
```bash
pip freeze > requirements.txt
```

---

## 🗄️ Database Setup

Run the following commands to set up your local database:
```bash
python manage.py makemigrations
python manage.py migrate
```

This will create a fresh `db.sqlite3` file locally. It is ignored in the repo to keep things clean and portable.

---

## 🚀 Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the app.

---

## 🔒 Ignored Files

This project uses a `.gitignore` file to exclude sensitive or unnecessary files from version control. Here's what's ignored:

- `db.sqlite3`: Local database file. Each user should create their own using `migrate`.
- `env/`: Virtual environment folder.
- `__pycache__/`: Python cache files.
- `.vscode/`: Editor-specific settings.
- `*.pyc`: Compiled Python files.
- `.DS_Store`, `Thumbs.db`: OS-specific junk files.

These exclusions keep the repository clean and prevent machine-specific issues.

---

## 🙌 Contributing

Feel free to fork the repo, make changes, and submit pull requests. This project is for learning, collaboration, and experimentation.

---

## 📬 Contact

If you run into issues or want to suggest improvements, feel free to reach out via GitHub or open an issue.

Happy coding!
