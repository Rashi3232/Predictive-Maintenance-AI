# Predictive Maintenance for Industrial Equipment using Artificial Intelligence

## Project Overview

This project is an AI-based Predictive Maintenance System developed using Python and Machine Learning. It predicts whether industrial equipment is likely to fail by analyzing sensor data such as temperature, vibration, pressure, and humidity.

The system helps industries reduce downtime by detecting potential failures before they occur and recommending maintenance actions.

---

## Problem Statement

Industrial facilities often face unexpected equipment failures, leading to production losses and increased maintenance costs.

This project predicts equipment failures in advance using Machine Learning, enabling proactive maintenance.

---

## Features

- Predict equipment failures using Machine Learning
- Analyze sensor data
- Real-time monitoring simulation
- Automatic maintenance alerts
- Maintenance recommendations
- Interactive Streamlit dashboard

---

## Technologies Used

- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## Project Structure

```
Predictive_Maintenance_AI/
│
├── dashboard.py
├── train_model.py
├── realtime_monitor.py
├── dataset.csv
├── predictive_model.pkl
├── requirements.txt
├── Predictive_Maintenance_Project_Report.pdf
├── Predictive_Maintenance_Project_Report.docx
└── README.md
```

---

## Dataset

The dataset contains the following sensor values:

| Feature | Description |
|----------|-------------|
| Temperature | Machine Temperature |
| Vibration | Machine Vibration |
| Pressure | Internal Pressure |
| Humidity | Environmental Humidity |
| Failure | 0 = Healthy, 1 = Failure |

---

## Machine Learning Algorithm

This project uses the **Random Forest Classifier** because it:

- Provides high accuracy
- Handles tabular sensor data effectively
- Reduces overfitting
- Supports fast predictions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rashi3232/Predictive-Maintenance-AI.git
```

Move to the project folder:

```bash
cd Predictive-Maintenance-AI
```

Install the required libraries:

```bash
py -m pip install -r requirements.txt
```

---

## Run the Project

### Step 1: Train the Model

```bash
py train_model.py
```

This creates the trained model file:

```
predictive_model.pkl
```

---

### Step 2: Run Real-Time Monitoring

```bash
py realtime_monitor.py
```

---

### Step 3: Launch the Dashboard

```bash
py -m streamlit run dashboard.py
```

The dashboard will open in your browser at:

```
http://localhost:8501
```

---

## Example Output

### Healthy Machine

```
Equipment is Healthy
```

### Failure Detected

```
⚠ Equipment Failure Predicted

Recommendation:
- Perform Immediate Inspection
- Check Bearings
- Lubricate Moving Parts
- Replace Faulty Components
```

---

## Advantages

- Reduces equipment downtime
- Predicts failures early
- Improves maintenance planning
- Reduces maintenance costs
- Increases equipment life
- Improves productivity

---

## Future Scope

- IoT Sensor Integration
- Cloud-Based Monitoring
- Email and SMS Alerts
- Deep Learning Models
- Mobile Application
- Remaining Useful Life (RUL) Prediction

---

## Author

**Rashi Goel**

B.Tech CSE (AI & ML)

---

## License

This project is developed for educational and academic purposes.
