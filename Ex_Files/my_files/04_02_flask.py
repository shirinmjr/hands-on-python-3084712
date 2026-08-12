import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()

    for laureate in laureates:
        surname = laureate["surname"].lower()
        first_name = laureate["name"].lower()
        if (search_string in surname) or (search_string in first_name):
            results.append(laureate)

    return jsonify(results)


app.run(debug=True) 

# NOTES:
# Run the Flask application in debug mode, which provides helpful error messages and auto-reloads the server on code changes
# To start you need to install Flask, you can do this by running the following command in your terminal:
# python3 -m pip install Flask