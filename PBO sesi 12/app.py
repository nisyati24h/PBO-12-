from flask import Flask, render_template, request, redirect

from models.user import User
from models.task_manager import TaskManager
from models.screen_time_tracker import ScreenTimeTracker

app = Flask(__name__)

user = User("Nisya", 5)

tracker = ScreenTimeTracker()

tasks = TaskManager()

tasks.add_task("Tugas PBO")
tasks.add_task("Tugas AI")

tracker.add_record("2026-06-24", 3)

# DASHBOARD
@app.route("/")
def home():

    return render_template(
        "index.html",
        username=user.get_username(),
        limit=user.get_screen_limit(),
        screentime=tracker.get_total_time(),
        taskcount=tasks.task_count()
    )

# SCREEN TIME PAGE
@app.route("/screen_time")
def screen_time():

    return render_template(
        "screen_time.html",
        records=tracker.get_records(),
        total_time=tracker.get_total_time(),
        limit=user.get_screen_limit()
    )

# REMINDER PAGE
@app.route("/reminder")
def reminder():

    reminders = [
        "Kerjakan tugas sebelum deadline",
        "Istirahat setelah 1 jam belajar",
        "Kurangi screen time berlebihan"
    ]

    return render_template(
        "reminder.html",
        reminders=reminders
    )

# TAMBAH SCREEN TIME
@app.route("/add_time", methods=["POST"])
def add_time():

    date = request.form["date"]
    hours = request.form["hours"]

    tracker.add_record(date, hours)

    return redirect("/screen_time")

# TASK MANAGER
@app.route("/tasks")
def task_page():

    return render_template(
        "tasks.html",
        tasklist=tasks.get_tasks()
    )

@app.route("/add_task", methods=["POST"])
def add_task():

    task = request.form["task"]

    tasks.add_task(task)

    return redirect("/tasks")

# REPORT
@app.route("/report")
def report():

    return render_template(
        "report.html",
        records=tracker.get_records(),
        total_time=tracker.get_total_time()
    )
@app.route("/team")
def team():

    members = [
        {
            "nama":"Nisya Lathifah",
            "nim":"20240040087"
        },
        {
            "nama":"Neng Sahla Nurul Fauziah",
            "nim":"20240040130"
        },
        {
            "nama":"Neng Shifa Aulia Sutisna",
            "nim":"20240040120"
        },
        {
            "nama":"Novia Putri Wardani",
            "nim":"20240040089"
        }
    ]

    return render_template(
        "team.html",
        members=members
    )

if __name__ == "__main__":
    app.run(debug=True)