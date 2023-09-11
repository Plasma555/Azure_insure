

from flask import Flask, render_template, request, jsonify
import requests,json

app = Flask(__name__)

# Define the Azure ML real-time endpoint URL and API key
AZURE_ML_ENDPOINT = "https://insurance-premium-xiqdj.eastus2.inference.ml.azure.com/score"
API_KEY = "zdasQ53jO8CjXjde130E3EBQXIUuGvEj"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve form data
        age = float(request.form["Age"])
        bmi = float(request.form["Bmi"])
        gender = request.form["Gender"]
        region = request.form["region"]
        smoker = request.form["smoker"]
        children = float(request.form["Children"])

        # Create the input data dictionary
        data = {
            "age": [age],
            "sex": [gender],
            "bmi": [bmi],
            "region": [region],
            "children": [children],
            "smoker": [smoker]
        }

        # Set up the headers with the API key
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + API_KEY
        }

        # Make a POST request to the Azure ML real-time endpoint for predictions
        response = requests.post(AZURE_ML_ENDPOINT, json=data, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            prediction = data[0]
            return render_template("index.html", prediction_text=f"Predicted Premium: ${prediction}")
        else:
            error_message = "Prediction request failed"
            return render_template("index.html", error=error_message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
