from flask import Flask, redirect, render_template, request, session
from task import Task
from datetime import datetime
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
   session.clear()
   return redirect("/add_task")

@app.route('/add_task', methods=["GET", "POST"])
def add_task():
   if request.method == "GET":
    date = datetime.now()
    # print(date)
    return render_template("add_task.html", date=date)
   
   name = request.form.get("name")
   description = request.form.get("description")
   date = request.form.get("date")
   estimated_time_to_finish = request.form.get("date")

   task = Task(name, date, estimated_time_to_finish, description)
   print(task)
   return redirect("/add_task")

