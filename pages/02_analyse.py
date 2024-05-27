import streamlit as st
import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import variables from 01_data.py in the pages package
from pages import data 
st.subheader('LAnalyse des données')

# Statistiques descriptives
st.subheader('Statistiques Descriptives')
st.write(data.nbres_users_by_country.describe())

# Corrélation
st.subheader('Matrice de Corrélation')
correlation_matrix = data.nbres_users_by_country.corr()
st.write(correlation_matrix)
plt.figure(figsize=(10, 5))
sns.heatmap(correlation_matrix, annot=True)
st.pyplot(plt)

# Visualisation - Nombre d'utilisateurs actifs par pays et mois
st.subheader('Visualisation des Données')
fig, ax = plt.subplots()
# Assurez-vous que 'nbres_users_by_country' est le DataFrame approprié
sns.barplot(data=data.nbres_users_by_country, x='country', y='activeUsers', ax=ax)
ax.set_title('Nombre d\'utilisateurs actifs par pays')
st.pyplot(fig)

# Visualisation - Durée d'engagement par pays
fig, ax = plt.subplots()
sns.barplot(data=data.temps_engagement_by_country, x='country', y='averageEngagementTime', ax=ax)
ax.set_title('Durée moyenne d\'engagement par pays')
st.pyplot(fig)

# Visualisation de la pivot table
st.subheader('Utilisateurs actifs par pays et par mois')
st.write(data.country_users_pivot)
plt.figure(figsize=(12, 8))
sns.heatmap(data.country_users_pivot, annot=True, fmt="d", cmap="viridis")
st.pyplot(plt)




