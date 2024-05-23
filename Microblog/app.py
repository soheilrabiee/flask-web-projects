from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime

# Create flask app
app = Flask(__name__)

# Database config
client = MongoClient("mongodb://localhost:27017")
app.db = client.microblog


# Endpoint might recieve POST and GET requests
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Taking the entry content
        entry_content = request.form.get("content")
        # Time of creation of the taken entry for datetime in html
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

        # Inserting data into our mongo database
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    # Formatted time for our design
    entries_with_date = [
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"),
        )
        for entry in app.db.entries.find()
    ]

    return render_template("home.html", entries=entries_with_date)
