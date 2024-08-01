from flask import Flask, render_template, request, redirect, url_for
from collections import defaultdict
import datetime

# Flask app
app = Flask(__name__)

habits = ["Test habit", "Test habit 2"]
# Default dict for habits if none creates a list for habits
completions = defaultdict(list)


@app.context_processor
def add_calc_date_range():
    """A function available to all the templates which calculates 3days after and before the selected date"""

    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}


@app.route("/")
def index():
    """Parses URL parameter to get date If the date is selected then creates a datetime object If not then uses today's date"""

    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template(
        "index.html",
        habits=habits,
        title="Habit Tracker - Home",
        completions=completions[selected_date],
        selected_date=selected_date,
    )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    """Takes the new habit from form and saves it if the method is POST"""

    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        selected_date=datetime.date.today(),
    )


# Same as <@app.route("/complete", methods=["POST"])>
@app.post("/complete")
def complete():
    """Adds the completed habit to the list and redirect user to the '/' with completed date"""
    date_string = request.form.get("date")
    habit = request.form.get("habitName")
    date = datetime.date.fromisoformat(date_string)
    completions[date].append(habit)

    return redirect(url_for("index", date=date_string))
