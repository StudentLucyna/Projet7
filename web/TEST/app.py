
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def root():
    message = "Hello from Flask"
    return render_template("message.html",msg=message)


if __name__ == "__main__":
    app.run()