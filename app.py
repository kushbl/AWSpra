from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("wine.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    fixedacidity=float(request.form.get("fa"))
    volatileacidity=float(request.form.get("va"))
    citricacid=float(request.form.get("ca"))
    residualsugar=float(request.form.get("rs"))
    chlorides=float(request.form.get("chl"))
    freesulfurdioxide=float(request.form.get("fsd"))
    totalsulfurdioxide=float(request.form.get("tsd"))
    density=float(request.form.get("den"))
    pH=float(request.form.get("ph"))
    sulphates=float(request.form.get("sul"))
    alcohol=float(request.form.get("al"))
    
    
    
    result=model.predict(np.array([[fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol]]))
    
    if result[0]==1:
        return "<h1>Good quality</h1>"
    else:
        return "<h1>Bad quality</h1>"


#app.run(debug=True,port=5001)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)