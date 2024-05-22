from flask import Flask, render_template, request
import datetime

# Create flask app
app = Flask(__name__)

entries = []


# Endpoint might recieve POST and GET requests
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Taking the entry content
        entry_content = request.form.get("content")
        # Time of creation of the taken entry for datetime in html
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))

    # Formatted time for our design
    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"),
        )
        for entry in entries
    ]

    return render_template("home.html", entries=entries_with_date)
