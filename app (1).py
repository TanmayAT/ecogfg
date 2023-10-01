from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model1 = pickle.load(open('model.pkl', 'rb'))  # Water quality model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_water_quality', methods=['POST'])
def predict_water_quality():
    ph = float(request.form['ph'])
    Hardness = float(request.form['Hardness'])
    Solids = float(request.form['Solids'])
    Chloramines = float(request.form['Chloramines'])
    Sulfate = float(request.form['Sulfate'])
    Conductivity = float(request.form['Conductivity'])
    Organic_carbon = float(request.form['Organic_carbon'])
    Trihalomethanes = float(request.form['Trihalomethanes'])
    Turbidity = float(request.form['Turbidity'])
    
    # Make predictions using the water quality model
    water_quality_prediction = model1.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])

    return render_template('index.html', water_quality_prediction=water_quality_prediction[0])

if __name__ == "__main__":

    app.run(debug=True)
