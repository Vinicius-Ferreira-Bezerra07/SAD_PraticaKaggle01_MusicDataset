import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# streamlit run <nome da aplicação>

# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import CountVectorizer

# Se baixar a base de dados para usar remotamente, alterar o caminho para o local onde esta a base baixada
# https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics?resource=download

dataBase = pd.read_csv("songs.csv")

# informações da database
# print(dataBase.info())
# print(dataBase.describe())

st.title("DataBase Songs - Streamlit")

# dataBase = pd.read_csv("/kaggle/input/music-dataset-song-information-and-lyrics/songs.csv")

# Grafico de Barras de musicas/generos
st.subheader("Distribuição de musicas por genero")
popularidade_artista = dataBase[['Artist', 'Popularity']]
popularidade_artista = popularidade_artista.groupby('Artist').sum()
print(popularidade_artista)
fig, ax = plt.subplots()
sns.barplot(x=popularidade_artista.index,
            y=popularidade_artista['Popularity'])

st.pyplot(fig)
