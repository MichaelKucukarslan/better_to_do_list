from flask import Flask
from task import Task

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Better to do list"

task1 = Task("Hello", "Date")

print("Original:")
print (task1._name)
print (task1.date)
print (task1.estimated_time_to_finish)
print (task1.notes)

print()

print("Name Changed:")
task1.set_name("Poop")
print(task1._name)

print(task1)