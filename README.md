
Built by https://www.blackbox.ai

---

```markdown
# Iris Flower Classification API

## Project Overview
Iris Flower Classification API is a web application built using Flask that utilizes a Support Vector Machine (SVM) classifier to predict the species of the Iris flower based on its sepal and petal measurements. The application allows users to input flower measurements and receive species predictions along with confidence probabilities.

## Installation

To install and run the project, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iris-flower-classification.git
   cd iris-flower-classification
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   Make sure you have `flask` and `scikit-learn` installed. Install them via pip:
   ```bash
   pip install flask scikit-learn
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   The application will be available at `http://localhost:8000`.

## Usage

1. Open your web browser and navigate to `http://localhost:8000`.
2. You will see the home page with options to navigate to the prediction page.
3. Enter the sepal and petal measurements of the Iris flower and submit the form.
4. The application will return the predicted species along with the confidence score and probabilities for all species.

## Features

- User-friendly web interface for inputting flower measurements.
- SVM classifier trained on the Iris dataset.
- Real-time prediction of the Iris flower species.
- Error handling for invalid input values.

## Dependencies

The following dependencies are required for this project:

- Flask: A micro web framework for Python.
- scikit-learn: A machine learning library for Python.

To install them, run:
```bash
pip install flask scikit-learn
```

## Project Structure

```
.
├── app.py               # Main application file
├── index.html           # Home page template
├── predict.html         # Prediction page template
└── results.html         # Results display page template
```

### Description of Project Files

- **app.py**: The main application file that contains the Flask API and SVM classifier logic.
- **index.html**: HTML template for the homepage where users can navigate to prediction.
- **predict.html**: HTML template for inputting measurements for prediction.
- **results.html**: HTML template for displaying the prediction results to the user.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```