from flask import Flask
from flask import render_template
from flask import request
from tipDistCalc import calculate_tip_share

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        raw_text = request.form["employees"] #get the input from the page and conver it to a string
        emp_dict = parse_employee_data(raw_text) #parse the raw_text into a form that is usable by the calculator
        total_tips = float(request.form["total_tips"]) #grab the total_tips input from the page
        results = calculate_tip_share(emp_dict, total_tips) #calculate the tip out
    
    return render_template("index.html")

def parse_employee_data(text):
    employee_info = {} #dictionary that will be populated with employee data

    lines = text.split("\n") #split lines at every new line

    for line in lines:
        name, hours = line.split(",") #split name and hours at each comma
        name = name.strip() #clean up the name
        hours = int(hours.strip()) #clean up the hours

        employee_info[name] = hours # assign the hours value to the key name

    return employee_info

app.run(debug=True)