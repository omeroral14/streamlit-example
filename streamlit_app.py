from collections import  namedtuple
import altair as alt
import math
import pandas as pd
from sklearn.tree import export_graphviz

st.title("Kaç yaşındasın")
dogum=st.number_input("Doğum Tarihiniz")
yas=2022-dogum
st.subheader(yas)
