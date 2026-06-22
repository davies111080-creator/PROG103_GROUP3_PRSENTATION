import tkinter as tk
from tkinter import ttk, messagebox
import itertools

# -----------------------------
# "Database" of 10 students
# -----------------------------
students_db = {
    "1000000001": {
        "name": "Abdul Kamara",
        "password": "Abdul1234",
        "faculty": "Computer Science",
        "fees": {"total": 2500, "paid": 2000},
        "grades": {
            "Programming I": "A",
            "Database Systems": "B+",
            "Discrete Math": "A-",
            "Computer Architecture": "B"
        },
        "timetable": {
            "Monday": "Programming I - 9:00\nDiscrete Math - 11:00",
            "Tuesday": "Database Systems - 10:00",
            "Wednesday": "Computer Architecture - 2:00",
            "Thursday": "Lab - 3:00",
            "Friday": "Free"
        }
    },
    "1000000002": {
        "name": "Mariam Conteh",
        "password": "Abdul12345",
        "faculty": "Business Administration",
        "fees": {"total": 2300, "paid": 1000},
        "grades": {
            "Accounting I": "B",
            "Business Law": "A",
            "Marketing": "B+",
            "Economics": "A-"
        },
        "timetable": {
            "Monday": "Accounting I - 8:00",
            "Tuesday": "Business Law - 10:00",
            "Wednesday": "Marketing - 1:00",
            "Thursday": "Economics - 9:00",
            "Friday": "Seminar - 3:00"
        }
    },
    "1000000003": {
        "name": "John Doe",
        "password": "Abdul123456",
        "faculty": "Engineering",
        "fees": {"total": 2700, "paid": 2700},
        "grades": {
            "Mechanics": "B+",
            "Thermodynamics": "A",
            "Calculus": "A-",
            "Materials Science": "B"
        },
        "timetable": {
            "Monday": "Mechanics - 9:00",
            "Tuesday": "Thermodynamics - 11:00",
            "Wednesday": "Calculus - 2:00",
            "Thursday": "Materials Science - 3:00",
            "Friday": "Workshop - 10:00"
        }
    },
    "1000000004": {
        "name": "Aisha Sesay",
        "password": "Abdul1234567",
        "faculty": "Nursing",
        "fees": {"total": 2600, "paid": 2000},
        "grades": {
            "Anatomy": "A",
            "Physiology": "B+",
            "Pharmacology": "B",
            "Nursing Ethics": "A-"
        },
        "timetable": {
            "Monday": "Anatomy - 8:00",
            "Tuesday": "Physiology - 10:00",
            "Wednesday": "Pharmacology - 1:00",
            "Thursday": "Nursing Ethics - 3:00",
            "Friday": "Clinical - 9:00"
        }
    },
    "1000000005": {
        "name": "Michael Smith",
        "password": "Abdul12345678",
        "faculty": "Computer Science",
        "fees": {"total": 2500, "paid": 1500},
        "grades": {
            "Programming I": "B",
            "Database Systems": "B",
            "Networks": "A-",
            "Operating Systems": "B+"
        },
        "timetable": {
            "Monday": "Programming I - 9:00",
            "Tuesday": "Networks - 11:00",
            "Wednesday": "Operating Systems - 2:00",
            "Thursday": "Database Systems - 3:00",
            "Friday": "Project - 10:00"
        }
    },
    "1000000006": {
        "name": "Fatmata Bangura",
        "password": "Fatmata11",
        "faculty": "Education",
        "fees": {"total": 2200, "paid": 2200},
        "grades": {
            "Curriculum Studies": "A-",
            "Educational Psychology": "B+",
            "Teaching Methods": "A",
            "Assessment": "B"
        },
        "timetable": {
            "Monday": "Curriculum Studies - 8:00",
            "Tuesday": "Educational Psychology - 10:00",
            "Wednesday": "Teaching Methods - 1:00",
            "Thursday": "Assessment - 3:00",
            "Friday": "Practicum - 9:00"
        }
    },
    "1000000007": {
        "name": "David Johnson",
        "password": "David7777",
        "faculty": "Law",
        "fees": {"total": 2800, "paid": 1800},
        "grades": {
            "Constitutional Law": "B+",
            "Criminal Law": "A-",
            "Contract Law": "B",
            "Legal Writing": "A"
        },
        "timetable": {
            "Monday": "Constitutional Law - 9:00",
            "Tuesday": "Criminal Law - 11:00",
            "Wednesday": "Contract Law - 2:00",
            "Thursday": "Legal Writing - 3:00",
            "Friday": "Moot Court - 10:00"
        }
    },
    "1000000008": {
        "name": "Sarah Brown",
        "password": "Sarah1234",
        "faculty": "Medicine",
        "fees": {"total": 3000, "paid": 2500},
        "grades": {
            "Biochemistry": "A-",
            "Pathology": "B+",
            "Microbiology": "A",
            "Physiology": "B"
        },
        "timetable": {
            "Monday": "Biochemistry - 8:00",
            "Tuesday": "Pathology - 10:00",
            "Wednesday": "Microbiology - 1:00",
            "Thursday": "Physiology - 3:00",
            "Friday": "Clinical - 9:00"
        }
    },
    "1000000009": {
        "name": "Ibrahim Koroma",
        "password": "Ibrahim99",
        "faculty": "Agriculture",
        "fees": {"total": 2400, "paid": 2400},
        "grades": {
            "Soil Science": "B+",
            "Crop Production": "A-",
            "Agricultural Economics": "B",
            "Animal Science": "A"
        },
        "timetable": {
            "Monday": "Soil Science - 9:00",
            "Tuesday": "Crop Production - 11:00",
            "Wednesday": "Agricultural Economics - 2:00",
            "Thursday": "Animal Science - 3:00",
            "Friday": "Field Work - 10:00"
        }
    },
    "1000000010": {
        "name": "Emily Davis",
        "password": "Emily8888",
        "faculty": "Computer Science",
        "fees": {"total": 2500, "paid": 1000},
        "grades": {
            "Programming II": "A",
            "Data Structures": "A-",
            "Web Development": "B+",
            "Software Engineering": "B"
        },
        "timetable": {
            "Monday": "Programming II - 9:00",
            "Tuesday": "Data Structures - 11:00",
            "Wednesday": "Web Development - 2:00",
            "Thursday": "Software Engineering - 3:00",
            "Friday": "Project - 10:00"
        }
    },
}

announcements = [
    "Welcome to the new Student Portal!",
    "Mid-semester exams start next week.",
    "Fees payment deadline is 30th June.",
    "Faculty meeting on Friday at 2 PM.",
    "New library resources have been added."
]

# -----------------------------
# Validation functions
# -----------------------------
def is_valid_student_id(student_id: str) -> bool:
    return student_id.isdigit() and 1 <= len(student_id) <= 10

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_capital = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_capital and has_digit

# -----------------------------
# Main Application
# -----------------------------
class StudentPortalApp:
    def __init__(self,
                 root):
        self.id_entry = None
        self.root = root
        self.root.title("Student Portal")
        self.root.geometry("900x600")
        self.root.resizable(True, True)

        self.colors = itertools.cycle([
            "#ff6b6b", "#feca57", "#1dd1a1", "#54a0ff", "#5f27cd", "#ff9ff3"
        ])

        self.current_student_id = None
        self.announcement_index = 0

        self.create_login_ui()
        self.animate_login_title()
        self.animate_background()

    # -------------------------
    # Login UI
    # -------------------------
    def create_login_ui(self):
        self.login_frame = tk.Frame(self.root, bg="#1e272e")
        self.login_frame.place(relwidth=1, relheight=1)

        self.title_label = tk.Label(
            self.login_frame,
            text="STUDENT PORTAL",
            font=("Segoe UI Black", 32, "bold"),
            bg="#1e272e",
            fg="#ff6b6b"
        )
        self.title_label.pack(pady=40)

        subtitle = tk.Label(
            self.login_frame,
            text="Login with your Student ID and Password",
            font=("Segoe UI", 13),
            bg="#1e272e",
            fg="#d2dae2"
        )
        subtitle.pack(pady=5)

        container = tk.Frame(self.login_frame, bg="#2f3640")
        container.pack(pady=40)

        id_label = tk.Label(
            container,
            text="Student ID:",
            font=("Segoe UI", 11),
            bg="#2f3640",
            fg="#f5f6fa"
        )
        id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.id_entry = tk.Entry(container, font=("Segoe UI", 11), width=28)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(
            container,
            text="Password:",
            font=("Segoe UI", 11),
            bg="#2f3640",
            fg="#f5f6fa"
        )
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.password_entry = tk.Entry(
            container, font=("Segoe UI", 11), width=28, show="*"
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(
            container,
            text="Login",
            font=("Segoe UI Semibold", 11),
            bg="#54a0ff",
            fg="white",
            activebackground="#2e86de",
            activeforeground="white",
            relief="flat",
            width=18,
            command=self.handle_login
        )
        login_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.info_label = tk.Label(
            self.login_frame,
            text="ID: digits only (max 10). Password: ≥8 chars, 1 capital letter, 1 number.",
            font=("Segoe UI", 9),
            bg="#1e272e",
            fg="#ced6e0"
        )
        self.info_label.pack(pady=5)

    # -------------------------
    # Animations
    # -------------------------
    def animate_login_title(self):
        next_color = next(self.colors)
        self.title_label.config(fg=next_color)
        self.root.after(500, self.animate_login_title)

    def animate_background(self):
        # Simple pulsing background color
        self.login_frame.config(bg="#1e272e")
        self.root.after(1000, lambda: self.login_frame.config(bg="#111827"))
        self.root.after(2000, self.animate_background)

    # -------------------------
    # Handle login
    # -------------------------
    def handle_login(self):
        student_id = self.id_entry.get().strip()
        password = self.password_entry.get().strip()

        if not is_valid_student_id(student_id):
            messagebox.showerror(
                "Invalid ID",
                "Student ID must contain only digits and must not be more than 10 characters."
            )
            return

        if not is_valid_password(password):
            messagebox.showerror(
                "Invalid Password",
                "Password must be at least 8 characters, contain a capital letter and a number."
            )
            return

        student = students_db.get(student_id)
        if student is None:
            messagebox.showerror("Login Failed", "Student ID not found.")
            return

        if password != student["password"]:
            messagebox.showerror("Login Failed", "Incorrect password.")
            return

        self.current_student_id = student_id
        messagebox.showinfo("Login Successful", f"Welcome, {student['name']}!")
        self.open_dashboard()

    # -------------------------
    # Dashboard UI
    # -------------------------
    def open_dashboard(self):
        self.login_frame.destroy()
        self.root.title("Student Portal - Dashboard")

        self.main_frame = tk.Frame(self.root, bg="#020617")
        self.main_frame.place(relwidth=1, relheight=1)

        # Top bar
        top_bar = tk.Frame(self.main_frame, bg="#0f172a", height=60)
        top_bar.pack(fill="x", side="top")

        title = tk.Label(
            top_bar,
            text="Student Dashboard",
            font=("Segoe UI Black", 20, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )
        title.pack(side="left", padx=20)

        logout_btn = tk.Button(
            top_bar,
            text="Logout",
            font=("Segoe UI", 10),
            bg="#ef4444",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            relief="flat",
            command=self.logout
        )
        logout_btn.pack(side="right", padx=20)

        # Navigation bar
        nav_bar = tk.Frame(self.main_frame, bg="#020617", width=180)
        nav_bar.pack(fill="y", side="left")

        btn_style = {
            "font": ("Segoe UI", 11),
            "bg": "#1f2937",
            "fg": "#e5e7eb",
            "activebackground": "#111827",
            "activeforeground": "#38bdf8",
            "relief": "flat",
            "width": 16,
            "height": 2
        }

        tk.Button(nav_bar, text="Profile", command=self.show_profile, **btn_style).pack(pady=8)
        tk.Button(nav_bar, text="Fees", command=self.show_fees, **btn_style).pack(pady=8)
        tk.Button(nav_bar, text="Grades", command=self.show_grades, **btn_style).pack(pady=8)
        tk.Button(nav_bar, text="Timetable", command=self.show_timetable, **btn_style).pack(pady=8)
        tk.Button(nav_bar, text="Announcements", command=self.show_announcements, **btn_style).pack(pady=8)

        # Content area
        self.content_frame = tk.Frame(self.main_frame, bg="#020617")
        self.content_frame.pack(fill="both", expand=True, side="right")

        self.show_profile()
        self.start_announcement_ticker()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # -------------------------
    # Profile Page
    # -------------------------
    def show_profile(self):
        self.clear_content()
        student = students_db[self.current_student_id]

        header = tk.Label(
            self.content_frame,
            text="Profile",
            font=("Segoe UI Semibold", 18),
            bg="#020617",
            fg="#e5e7eb"
        )
        header.pack(anchor="w", padx=20, pady=20)

        info_frame = tk.Frame(self.content_frame, bg="#020617")
        info_frame.pack(anchor="w", padx=40, pady=10)

        tk.Label(info_frame, text=f"Name: {student['name']}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)
        tk.Label(info_frame, text=f"Student ID: {self.current_student_id}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)
        tk.Label(info_frame, text=f"Faculty: {student['faculty']}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)

    # -------------------------
    # Fees Page
    # -------------------------
    def show_fees(self):
        self.clear_content()
        student = students_db[self.current_student_id]
        fees = student["fees"]
        balance = fees["total"] - fees["paid"]
        status = "Paid" if balance == 0 else "Not Fully Paid"
        color = "#22c55e" if balance == 0 else "#f97316"

        header = tk.Label(
            self.content_frame,
            text="Fees Information",
            font=("Segoe UI Semibold", 18),
            bg="#020617",
            fg="#e5e7eb"
        )
        header.pack(anchor="w", padx=20, pady=20)

        info_frame = tk.Frame(self.content_frame, bg="#020617")
        info_frame.pack(anchor="w", padx=40, pady=10)

        tk.Label(info_frame, text=f"Total Fees: ${fees['total']}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)
        tk.Label(info_frame, text=f"Amount Paid: ${fees['paid']}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)
        tk.Label(info_frame, text=f"Balance: ${balance}",
                 font=("Segoe UI", 12), bg="#020617", fg="#e5e7eb").pack(anchor="w", pady=4)
        tk.Label(info_frame, text=f"Status: {status}",
                 font=("Segoe UI Semibold", 12), bg="#020617", fg=color).pack(anchor="w", pady=4)

        tk.Button(
            info_frame,
            text="Mock Pay Now",
            font=("Segoe UI", 11),
            bg="#22c55e",
            fg="white",
            activebackground="#16a34a",
            activeforeground="white",
            relief="flat",
            command=lambda: messagebox.showinfo("Payment", "This is a mock payment button.")
        ).pack(anchor="w", pady=10)

    # -------------------------
    # Grades Page
    # -------------------------
    def show_grades(self):
        self.clear_content()
        student = students_db[self.current_student_id]

        header = tk.Label(
            self.content_frame,
            text="Module Grades",
            font=("Segoe UI Semibold", 18),
            bg="#020617",
            fg="#e5e7eb"
        )
        header.pack(anchor="w", padx=20, pady=20)

        grades_frame = tk.Frame(self.content_frame, bg="#020617")
        grades_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("module", "grade")
        tree = ttk.Treeview(grades_frame, columns=columns, show="headings", height=8)
        tree.pack(fill="both", expand=True)

        tree.heading("module", text="Module")
        tree.heading("grade", text="Grade")

        tree.column("module", width=400, anchor="w")
        tree.column("grade", width=100, anchor="center")

        for module, grade in student["grades"].items():
            tree.insert("", "end", values=(module, grade))

        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#020617",
            foreground="#e5e7eb",
            fieldbackground="#020617",
            rowheight=25
        )
        style.configure(
            "Treeview.Heading",
            background="#1e293b",
            foreground="#e5e7eb",
            font=("Segoe UI Semibold", 10)
        )
        style.map("Treeview", background=[("selected", "#1d4ed8")])

    # -------------------------
    # Timetable Page
    # -------------------------
    def show_timetable(self):
        self.clear_content()
        student = students_db[self.current_student_id]

        header = tk.Label(
            self.content_frame,
            text="Weekly Timetable",
            font=("Segoe UI Semibold", 18),
            bg="#020617",
            fg="#e5e7eb"
        )
        header.pack(anchor="w", padx=20, pady=20)

        table_frame = tk.Frame(self.content_frame, bg="#020617")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        colors = {
            "Monday": "#0ea5e9",
            "Tuesday": "#22c55e",
            "Wednesday": "#f97316",
            "Thursday": "#a855f7",
            "Friday": "#ef4444"
        }

        for day in days:
            day_frame = tk.LabelFrame(
                table_frame,
                text=day,
                font=("Segoe UI Semibold", 11),
                bg="#020617",
                fg=colors[day],
                bd=2
            )
            day_frame.pack(fill="x", pady=5)

            text = student["timetable"].get(day, "No classes")
            tk.Label(
                day_frame,
                text=text,
                font=("Segoe UI", 11),
                bg="#020617",
                fg="#e5e7eb",
                justify="left"
            ).pack(anchor="w", padx=10, pady=5)

    # -------------------------
    # Announcements Page
    # -------------------------
    def show_announcements(self):
        self.clear_content()

        header = tk.Label(
            self.content_frame,
            text="Announcements",
            font=("Segoe UI Semibold", 18),
            bg="#020617",
            fg="#e5e7eb"
        )
        header.pack(anchor="w", padx=20, pady=20)

        self.ann_frame = tk.Frame(self.content_frame, bg="#020617")
        self.ann_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.ann_label = tk.Label(
            self.ann_frame,
            text="",
            font=("Segoe UI", 13),
            bg="#020617",
            fg="#38bdf8"
        )
        self.ann_label.pack(anchor="w", pady=10)

        # Show current announcement immediately
        self.update_announcement_label()

    def start_announcement_ticker(self):
        # Runs regardless of which page is open
        self.root.after(0, self.rotate_announcements)

    def rotate_announcements(self):
        self.announcement_index = (self.announcement_index + 1) % len(announcements)
        self.update_announcement_label()
        self.root.after(3000, self.rotate_announcements)

    def update_announcement_label(self):
        # Update label only if announcements page is visible
        if hasattr(self, "ann_label") and self.ann_label.winfo_exists():
            self.ann_label.config(text=announcements[self.announcement_index])

    # -------------------------
    # Logout
    # -------------------------
    def logout(self):
        self.main_frame.destroy()
        self.current_student_id = None
        self.create_login_ui()


# -----------------------------
# Run the app
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPortalApp(root)
    root.mainloop()
