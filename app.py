from flask import Flask, render_template,jsonify,request 
from model3 import Predict
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict-form")
def predict_form():
    return render_template("predict.html")

@app.route("/predict", methods=["GET"])
def predict():
    try:
        carbon = float(request.args.get("carbon"))
        manganese = float(request.args.get("manganese"))
        silicon = float(request.args.get("silicon"))
        nickel = float(request.args.get("nickel"))
        chromium = float(request.args.get("chromium"))
        copper = float(request.args.get("copper"))
        iron = float(request.args.get("iron"))
        boron = float(request.args.get("boron"))
        molybdenum = float(request.args.get("molybdenum"))
        phosphorus = float(request.args.get("phosphorus"))
        sulfur = float(request.args.get("sulfur"))
        titanium = float(request.args.get("titanium"))
        vanadium = float(request.args.get("vanadium"))
        tin= float(request.args.get("tin"))
        zinc = float(request.args.get("zinc"))

        result = Predict(boron,carbon,chromium,copper,iron, manganese,molybdenum, nickel,phosphorus,sulfur, silicon, titanium, vanadium,tin,zinc)
        print(result)
        return render_template("predict.html",strength=result)

    except Exception as e:
        return f"Error: {e}"


if __name__=="__main__":
    app.run(debug=True)
