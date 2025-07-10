# 🧪 Material Strength Predictor

A sleek and intelligent web application powered by **Machine Learning + Flask** that predicts the **tensile strength** of a ferrous alloy based on its **chemical composition**. Whether you're an engineering student, researcher, or materials scientist — this tool gives you instant strength predictions from elemental inputs.Note that the output obtained is not fully accurate it has minor error due to smaller dataset provided for machine learning.

---

## 🚀 Features

✅ Predicts **Ultimate Tensile Strength (UTS)** in MPa  
✅ Input support for **15 chemical elements**  
✅ Clean, responsive UI (mobile + desktop friendly)  
✅ Powered by a trained **Random Forest Regressor**  
✅ 🔁 Dynamic result rendering using JavaScript & Flask

---

## ⚙️ Tech Stack

| Layer         | Technology                              |
| ------------- | --------------------------------------- |
| 🧠 ML Model   | RandomForestRegressor (scikit-learn)    |
| 🖥 Backend     | Python, Flask                           |
| 💅 Frontend   | HTML5, CSS3, JS                         |
| 📦 Dataset    | Real/simulated alloy compositions + UTS |
| 🌐 Deployment | [Render / Railway / Localhost]          |

---

## 🔢 Inputs

You can enter % composition of the following elements:

- Carbon (C)
- Manganese (Mn)
- Silicon (Si)
- Nickel (Ni)
- Chromium (Cr)
- Copper (Cu)
- Iron (Fe)
- Boron (B)
- Molybdenum (Mo)
- Phosphorus (P)
- Sulfur (S)
- Titanium (Ti)
- Vanadium (V)
- Tin (Sn)
- Zinc (Zn)

---

## 📷 Screenshots

<p align="center">
  <img src="https://your-screenshot-link.com/predict.png" width="700">
</p>

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/material-strength-predictor.git
cd material-strength-predictor

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
