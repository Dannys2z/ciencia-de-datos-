import sreeamlit as st 
import pandas as pd 
st.title("Titanic dataset")

data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
select_sex = st.selectbox("Select Sex", data["sex"].unique())

st.write(f"Select Option: {selected_sex!r}")
filtered_data_sex = [data["sex"] == selected_sex]
sr.dataframe(filtered_data_sex)