# Driver Consistency Index & Championship Probability Model (Formula 1)
## Project Goal

The goal of this project is to build a data-driven model that quantifies driver consistency and estimates championship-winning probabilities using historical Formula 1 data.

## Motivation

Predicting long-term outcomes in Formula 1 is difficult due to regulation changes, driver transfers, and random race events. 
Instead of predicting a single winner, this project focuses on modeling uncertainty by analyzing historical performance trends of drivers and constructors.


A machine learning + simulation dashboard that predicts **race win probabilities** and **championship outcomes** using historical Formula 1 data.

Built with **XGBoost, SHAP, and Streamlit**.

---

## 🚀 Features

✅ Driver win probability prediction  
✅ Monte Carlo championship simulation  
✅ SHAP model explanations (feature importance per driver)  
✅ Interactive Streamlit dashboard  
✅ Clean feature-engineered dataset  

---

## 📊 Model

The model uses engineered features such as:

- Grid position  
- Rolling average finish  
- Constructor cumulative points  

Algorithm:
- XGBoost Classifier

Interpretability:
- SHAP (feature contribution explanations)

---

## 🖥️ Demo (Run locally)

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
F1 Championship Model/
│
├── app.py                  # Streamlit dashboard
├── model.pkl               # trained model
├── requirements.txt
├── data/
│   └── final_model_data.csv
└── notebooks/
```

---

## 🎯 Motivation

Formula 1 outcomes are highly uncertain due to:
- regulation changes
- driver transfers
- race incidents

Instead of predicting a single winner, this project models **probabilities and uncertainty**, giving a more realistic view of championship chances.

---

## 🛠️ Tech Stack

- Python
- Pandas / NumPy
- XGBoost
- SHAP
- Streamlit
- Matplotlib

---

## 📌 Future Improvements

- Add race filter selector
- Add season simulation
- Deploy to Streamlit Cloud
- Improve feature engineering
- Add live data

---



