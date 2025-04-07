from flask import Flask, render_template, request, jsonify
from sklearn import datasets, svm
import numpy as np

app = Flask(__name__)

# Load and prepare Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train SVM classifier
clf = svm.SVC(probability=True)
clf.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/results')
def results_page():
    return render_template('results.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
        
        # Validate input ranges (approximate Iris dataset ranges)
        if (features[0] < 4 or features[0] > 8 or 
            features[1] < 2 or features[1] > 4.5 or
            features[2] < 1 or features[2] > 7 or
            features[3] < 0.1 or features[3] > 2.5):
            return jsonify({'error': 'Values outside valid range'}), 400
            
        prediction = clf.predict([features])[0]
        probabilities = clf.predict_proba([features])[0]
        
        return jsonify({
            'species': iris.target_names[prediction],
            'confidence': float(probabilities[prediction]),
            'probabilities': {
                'setosa': float(probabilities[0]),
                'versicolor': float(probabilities[1]),
                'virginica': float(probabilities[2])
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)