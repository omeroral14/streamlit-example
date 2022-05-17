import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.tree import export_graphviz

st.title("Kaç yaşındasın")
dogum=st.number_input("Doğum Tarihiniz")
yas=2022-dogum
st.subheader(yas)
