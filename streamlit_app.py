import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.tree import export_graphviz

pokemon=pd.read_csv("pokemon.csv")
combats=pd.read_csv("combats.csv")

col1,col2,col3=st.columns(3)

with col1:
    poke1=st.selectbox("İlk Pokemon", pokemon['Name'])
    isim=poke1.lower()
    isim="images/images/"+isim+".png"
    st.image(isim)
    poke1 = int(pokemon[pokemon["Name"] == poke1]["#"])


with col2:
    st.image("https://www.nicepng.com/png/full/271-2712237_vs-rooster-teeth.png")

with col3:
    poke2 = st.selectbox("İkinci Pokemon", pokemon['Name'])
    isim = poke2.lower()
    isim = "images/images/" + isim + ".png"
    st.image(isim)
    poke2 = int(pokemon[pokemon["Name"] == poke2]["#"])

combats['Winner']=combats['First_pokemon']==['Winner']
combats['Winner']=np.where(combats['Winner']==True , 0 , 1)

y=combats[["Winner"]]
x=combats[["First_pokemon","Second_pokemon"]]
tree=DecisionTreeClassifier()
model=tree.fit(x,y)
skor=model.score(x,y)
tahmin=model.predict([[poke1,poke2]])

kol1,kol2,kol3=st.columns(3)

with kol1:
    st.write("")
with kol2:
    buton=st.button("Başlat")
    if buton:
        if tahmin==0:
            st.header("Kazanan")
            st.subheader(isim1)
        else:
            st.header("Kazanan")
            st.subheader(isim2)
        st.balloons()
