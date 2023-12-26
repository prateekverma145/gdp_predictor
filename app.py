import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd
from PIL import Image
path="model.pkl"
with open(path, 'rb') as f:
    model = pkl.load(f)
st.set_page_config(page_title="GDP Predictor",page_icon="🧊",layout="wide",initial_sidebar_state="expanded")


# Load an image from your local file system


st.markdown("<h1 style='text-align: center; color: white;'>GDP Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>A simple web app to predict the GDP per capita of a country</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Green;'>Made by Prateek Verma</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Github:<a href='https://github.com/prateekverma145'>prateekverma145</a></h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>LinkedIn:<a href='https://www.linkedin.com/in/prateek-verma-2a202b287'>prateek-verma</a></h4>", unsafe_allow_html=True)

link= "https://www.kaggle.com/fernandol/countries-of-the-world"
st.markdown(f"For more information about the dataset, visit {link}")
df=pd.read_csv('gdp_cleaned.csv')
ds=df.sample(3)

st.subheader("Small sample of the dataset")  
st.dataframe(ds)
st.warning("if you leave any value blank, the model will automatically fill mean value of that column!!")

st.subheader("Enter the values to predict the GDP")

a=st.text_input(key=1,label="Enter country name")
b=st.text_input(key=2,label="Enter Region")
c=st.text_input(key=3,label="Enter Population")
d=st.text_input(key=4,label="Enter area(sq.mi.)")
e=st.text_input(key=5,label="Enter Pop. Density(per sq.mi.)")
f=st.text_input(key=6,label="Enter Coastline (coast/area ratio)")
g=st.text_input(key=7,label="Enter Net migration")
h=st.text_input(key=8,label="Enter Infant mortality (per 1000 births)")
z=st.text_input(key=20,label="enter Literacy(%)")
i=st.text_input(key=9,label='Phones (per 1000)')
j=st.text_input(key=10,label="Enter Arable (%)")
k=st.text_input(key=11,label="Enter Crops (%)")
l=st.text_input(key=12,label="Enter Other (%)")
m=st.selectbox("Select the climate value",df['Climate'].unique())   
n=st.text_input(key=14,label="Enter Birthrate")
o=st.text_input(key=15,label="Enter Deathrate")
p=st.text_input(key=16,label="Enter Agriculture")
q=st.text_input(key=17,label="Enter Industry")
r=st.text_input(key=18,label="Enter Service")
arr=np.array([c,d,e,f,g,h,z,i,j,k,l,m,n,o,p,q,r]).reshape(1,-1)
l=[]
          
            
if st.button("Predict GDP"):
    c=0
    if m=='':
        m=2
    for i in arr:
        for j in i:
            if j=='':
                j=np.nan
            l.append(j)     
    try:        
        res=model.predict(np.array(l).reshape(1,-1))
    except:
        st.error("Please enter all the values or something went wrong")
        res=-1
    finally:        
        st.subheader(f"The GDP per capita {a} is {int(res)} billion dollars")
        
 