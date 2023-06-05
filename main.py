import numpy as np
import pandas as pd
import streamlit as st

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

import seaborn as sns


#Se baixar a base de dados para usar remotamente, alterar o caminho para o local onde esta a base baixada
#https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics?resource=download
dataBase = pd.read_csv("songs.csv")

# dataBase = pd.read_csv("/kaggle/input/music-dataset-song-information-and-lyrics/songs.csv")

sns.histplot(dataBase, x='Popularity', kde=True, color='g')
