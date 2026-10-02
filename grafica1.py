import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as ptl 

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(titanic_data)
st.header("Data Description")

fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)

fig3,ax3 = ptl.subplots()
ax3.sacatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del titanic")
st.pyplot(fig3)