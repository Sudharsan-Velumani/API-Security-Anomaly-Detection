from flask import Flask, jsonify, request

app = Flask(__name__)

# A mock function to simulate predictions
def predict(data):
    return "anomalous" if sum(data) % 2 == 0 else "normal"

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        content = request.json
        if 'data' not in content:
            return jsonify({"error": "Missing 'data' in request"}), 400
        
        data = content['data']
        if not isinstance(data, list):
            return jsonify({"error": "'data' must be a list"}), 400
        
        prediction = predict(data)
        return jsonify({"prediction": prediction}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "API is working!"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
