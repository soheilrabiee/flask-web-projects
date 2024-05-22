from flask import Flask, render_template, request
import datetime

# Create flask app
app = Flask(__name__)


# Endpoint might recieve POST and GET requests
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Taking the entry content
        entry_content = request.form.get("content")
        # Time of creation for the taken entry
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        print(entry_content, formatted_date)
    return render_template("home.html")
