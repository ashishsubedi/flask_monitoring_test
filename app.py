from flask import Flask
import flask_monitoringdashboard as dashboard
import random
from time import sleep

app = Flask(__name__)
dashboard.bind(app)

@app.route('/')
def index():
    sleep(random.randint(1,10))
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
