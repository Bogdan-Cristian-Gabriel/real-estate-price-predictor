import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
df = pd.read_csv("Data.csv")

df["Construction year"] = pd.to_numeric(df["Construction year"], errors='coerce')
df["Area"] = pd.to_numeric(df["Area"], errors='coerce')

df["Age"] = 2026 - df["Construction year"]

varste_calc = df.groupby("Location")["Age"].transform("median")
df["Age"] = df["Age"].fillna(varste_calc)
df["Age"] = df["Age"].fillna(df["Age"].median())

df = df.dropna(subset=["Area"])
df = df[(df["Price"] >= 15000) & (df["Price"] <= 500000) & (df["Area"] >= 15) & (df["Rooms"] <= 10)]
df = df.drop(columns=["Construction year"])

df = pd.get_dummies(df, columns=["Location"], drop_first=True)

print(df.describe())
print(df.head())

Y = df["Price"]
X = df.drop(columns=["Price"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

print("MAE: ", mean_absolute_error(y_test, y_pred))
print("MSE: ", mean_squared_error(y_test, y_pred))

import pandas as pd


apartament_nou = pd.DataFrame(0, index=[0], columns=X_train.columns)

apartament_nou['Area'] = float(input("Apartment surface:"))
apartament_nou['Rooms'] = int(input("Number of Rooms:"))
apartament_nou['Age'] = int(input("Age of the apartment:"))

locatie_inp = input("Locatie:")
locatie = "Location_" + locatie_inp
apartament_nou[locatie] = 1

pred_price = rf_model.predict(apartament_nou)[0]
print(f'Pretul acestui apartament este: {pred_price:,.2f} EUR')