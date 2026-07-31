from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from tipDistCalc import calculate_tip_share

app = Flask(__name__)
app.secret_key = "super-secret-key-change-this-later" #needed for flash messages

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    if request.method == "POST":
        raw_text = request.form["employees"] #get the input from the page and convert it to a string
        emp_dict = parse_employee_data(raw_text) #parse the raw_text into a form that is usable by the calculator
        total_tips = float(request.form["total_tips"]) #grab the total_tips input from the page
        results = calculate_tip_share(emp_dict, total_tips) #calculate the tip out
    
    return render_template("index.html", payouts=results)

def parse_employee_data(text):
    employee_info = {} #dictionary that will be populated with employee data

    lines = text.split("\n") #split lines at every new line

    for line in lines:
        line = line.strip()
        if not line:
            continue #ignore any blank lines

        if "," not in line:
            flash(f"⚠️ Could not process '{line}'. Make sure it follows 'Name, Hours' format (e.g. Ted, 8).", "warning")
            continue

        name, hours = line.split(",", 1) #split name and hours at each comma
        name = name.strip() #clean up the name
        try:
            hours = float(hours.strip()) #clean up the hours and allow for portion of an hour to be calculated/entered
            employee_info[name] = hours # assign the hours value to the key name
        except ValueError:
            flash(f"⚠️ Invalid hours for '{name}. Please enter a valid number for hours worked.", "warning")

    return employee_info

app.run(debug=True)