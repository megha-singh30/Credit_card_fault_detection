import pickle
from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from models import *

application = Flask(__name__)
app = application

# 1. First step is to read the pickle files for Pre-processing and then model training
model = pickle.load(open('models/nb_model.pkl','rb'))
scale = pickle.load(open('models/StandardScaler.pkl','rb'))

# 2. Create Home page
@app.route("/")

def index():
    return render_template('index.html')

# 3. For the prediction page
@app.route('/predictdata',methods = ['GET','POST'])
def predict_data():
    if request. == 'POST':
        pass
    else:
        return render_template('home.html')
if __name__=="__main__":
    app.run(host="0.0.0.0")