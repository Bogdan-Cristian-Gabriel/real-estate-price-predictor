from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import pickle as pkl

df = pd.read_csv("Data.csv")

#COnverting to numeric
df["Construction year"] = pd.to_numeric(df["Construction year"], errors='coerce')
df["Area"] = pd.to_numeric(df["Area"], errors='coerce')

#Calculating the age of the apartment in a new column
df["Age"] = 2026 - df["Construction year"]

#Filling the blank spots with the median age
age_calc = df.groupby("Location")["Age"].transform("median")
df["Age"] = df["Age"].fillna(age_calc)
df["Age"] = df["Age"].fillna(df["Age"].median())

df = df.dropna(subset=["Area"])
df = df[(df["Price"] >= 15000) & (df["Price"] <= 500000) & (df["Area"] >= 15) & (df["Rooms"] <= 10)]
df = df.drop(columns=["Construction year"])

#Adding the dummies for the location
df = pd.get_dummies(df, columns=["Location"], drop_first=True)

print(df.describe())
print(df.head())

#Splitting the data into two
Y = df["Price"]
X = df.drop(columns=["Price"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Training and testing the model
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

#Calculating the errors
print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", mean_squared_error(y_test, y_pred))

#Exporting the trained model
with open("model.pkl", "wb") as f:
    pkl.dump(rf_model, f)
