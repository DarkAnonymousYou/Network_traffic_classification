import numpy as np
from flask import Flask, request, jsonify, render_template
import dill
import dill
from sklearn.utils.validation import check_X_y, check_array
from sklearn.utils.validation import check_X_y, check_array
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mutual_info_score
import numpy as np

app = Flask(__name__)

with open('hybrid_model.pkl', 'rb') as file:
    loaded_model = dill.load(file)

@app.route('/')
def view():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    data1 = int(request.form["sourcePort"])
    data2 = int(request.form["destinationPort"])
    data3 = int(request.form["natSourcePort"])
    data4 = int(request.form["natDestinationPort"])
    data5 = int(request.form["bytes"])
    data6 = int(request.form["bytesSent"])
    data7 = int(request.form["bytesReceived"])
    data8 = int(request.form["packets"])
    data9 = int(request.form["elapsedTime"])
    data10 = int(request.form["pktsSent"])
    data11 = int(request.form["pktsReceived"])

    # Prepare the data for prediction
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]])
    
    # Predict the result
    output = loaded_model.predict(arr)
    print(output)

    # Generate the prediction result
    if output == [0]:
        result = "Prediction result is to Allow"
    elif output == [1]:
        result = "Prediction result is to Deny"
    elif output == [2]:
        result = "Prediction result is to Drop"
    elif output == [3]:
        result = "Prediction result is to Reset-both"
    else:
        result = "You Entered Wrong Input"

    # Return the result as a response
    return render_template('predict.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
