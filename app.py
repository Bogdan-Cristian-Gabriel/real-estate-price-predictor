import streamlit as st
import pandas as pd
import pickle as pkl
st.title("Apartment price predictor")

st.write("Enter your data:")

model = pkl.load(open('model.pkl', 'rb'))

apartament = pd.DataFrame(data=0, index=[0], columns=model.feature_names_in_)

#Getting the data for the new apartment
apartament['Area'] = st.number_input("Area")
apartament['Age'] = st.number_input("Age")
apartament['Rooms'] = st.number_input("Number Of Rooms")
location = st.selectbox("Pick location", [col.split(sep="_")[1] for col in model.feature_names_in_ if col.startswith("Location_")])

apartament["Location_" + location] = 1
#Predicting the price of the apartment
if st.button("**Predict Price**"):
    price = model.predict(apartament)
    st.write("The estimated price of your apartment is :")
    st.write(f"{price[0]:,.2f} EUR")
