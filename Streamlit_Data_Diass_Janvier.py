import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
#import plotly.express as px


data = pd.read_csv("data_diass_janvier.csv")

st.write("Données brutes :")
st.write(data)


st.write("Graphes interactifs :")
st.line_chart(data['Plant Energy (kWh)'])

st.write("Graphes en barre :")
st.bar_chart(data['Plant Energy (kWh)'])

st.write("Graphes en area :")
st.area_chart(data,  x="Plant Energy (kWh)", y="Plant Power (kW)")



#st.scatter_chart(data,  x="Plant Energy (kWh)" )


# Graphique interactif avec plotly
#fig = px.scatter_matrix(data, dimensions=data.columns, title='Matrice de dispersion interactive')
#st.plotly_chart(fig)
