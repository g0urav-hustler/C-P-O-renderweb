# import flask
from flask import Flask, render_template, request
import urllib
import json
import os
app = Flask(__name__)
# model = pickle.load(open("models/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        data = {
        "nitrogen" : int(request.form["nitrogen"]),
        "phosphorus" : int(request.form["phosphorus"]),
        "potassium" : int(request.form["potassium"]),
        "temperature" : int(request.form["temperature"]),
        "humidity" : int(request.form["humidity"]),
        "ph" : int(request.form["ph"]),
        "rainfall" : int(request.form["rainfall"])

        }
        data = json.dumps(data)

        # Convert to String
        data = str(data)

        # Convert string to byte
        data = data.encode('utf-8')

        url = "https://48r4nqrd1l.execute-api.us-east-1.amazonaws.com/Crop-production-api/predict_func"

        # # Post Method is invoked if data != None
        # req =  urllib.request.Request(url, data=data)

        # # Response
        resp = urllib.request.urlopen(url= url, data = data)

        crop_predict = resp.read().decode()
        

        # crop_predict = model.predict([[nitrogen, phosphorus, potassium,temperature, humidity, ph, rainfall]])[0]
        crop_predict = crop_predict.capitalize()
        
        return render_template("index.html", prediction_text = "The best crop you should grow is {} .".format(crop_predict))
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug = True, port = port)
