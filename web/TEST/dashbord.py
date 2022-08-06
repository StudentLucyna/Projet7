
import pandas as pd
import streamlit as st
from flask import Flask, render_template
from PIL import Image
import plotly.express as px
import json
import plotly

app = Flask(__name__)

@app.route('/')
#def index():
    #return "Hello world !"

#API_URL = "http://127.0.0.1:5000/dashbord/"


def show_index():
    logo=Image.open('logo.png')
    st.image(logo, width=280)
    return render_template('index.html', logo=logo)           

def index():
        df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges",   
        "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
        })
        fig = px.bar(df, x="Fruit", y="Amount", color="City",
                 barmode="group")
        st.title('Hello Streamlit')
        st.write('''
            Streamlit: A web application framework for Python.
        ''')
        st.plotly_chart(fig)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('index.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run()