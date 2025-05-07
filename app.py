import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mi primer gráfico con Streamlit")

data = pd.DataFrame({
    "A": [10, 20, 30, 40],
    "B": [1, 3, 2, 4]
})

st.write("Datos:", data)

fig, ax = plt.subplots()
ax.plot(data["A"], data["B"])
st.pyplot(fig)
