ML Phishing Website Detection
---
Python 3.11.9 (Currently Using)

How to Run
---
1. Clone the repository:
--
git clone https://github.com/ramyabhat03/ML-Phishing-website-detection.git
cd ML-Phishing-website-detection

Create a virtual environment:
--
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate

Install requirements:
--
pip install -r requirements.txt

Run the Streamlit App
--
streamlit run app.py
Open your browser and enter any URL to check if it is phishing or legitimate.

Train the Model (Optional)
To retrain the model from the dataset:
--
python phishing_url_detector.py
This will extract features, train a new Random Forest model, evaluate it, and save it as phishing_model.pkl.

Tech Stack
--
Python
Scikit-learn
Pandas, NumPy
Streamlit
Joblib

Project Structure
--
ML-Phishing-website-detection/
│
├── datasets/
│   └── URL_dataset.csv         - Dataset used for training
├── phishing_model.pkl          - Trained model file
├── feature_extraction.py       - Script for extracting URL features
├── phishing_url_detector.py    - Script for model training and prediction
├── app.py                      - Streamlit frontend
└── README.md                   - Project documentation
