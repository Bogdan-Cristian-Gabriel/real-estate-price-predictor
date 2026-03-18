# 🏠 Apartment Price Predictor (Constanța & Seaside)

This project is an interactive web application that uses **Machine Learning** to predict the prices of apartments and houses in the Constanța, Mamaia, and Năvodari area, based on real estate market data.

## 🚀 Features
* **Real-Time Predictions:** Estimates real estate prices based on surface area, number of rooms, building age, and specific location.
* **Advanced Algorithm:** Powered by a `RandomForestRegressor` model trained to capture non-linear patterns in the real estate market (e.g., the "luxury premium" for exclusive areas like Faleza Nord or Mamaia).
* **Interactive Web Interface:** Built entirely in Python using the Streamlit library, offering a clean and user-friendly experience.
* **Feature Importance Analysis:** Highlights the top driving factors behind property prices in the region through interactive charts.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`RandomForestRegressor`, `StandardScaler`)
* **Web Framework:** Streamlit
* **Model Serialization:** Pickle (`pkl`)

## 📂 Project Structure
* `analysis.py` - The script used for Data Cleaning, Feature Engineering (calculating building age, handling missing values), and model training.
* `model.pkl` - The serialized Random Forest model saved after training.
* `app.py` - The source code for the Streamlit web interface.
* `Data.csv` - The raw dataset containing real estate listings (if made public).

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Bogdan-Cristian-Gabriel/real-estate-price-predictor/]
   cd real-estate-price-predictor
