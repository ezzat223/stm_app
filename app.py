import streamlit as st
import pandas as pd
from models.dummies import *
import joblib

model=joblib.load('models\model.h5')
scaler=joblib.load('models\scaler.h5')


st.title('Bikes Renting Project')
st.info('Just buiding a model')

col1,col2,col3=st.columns(3)
col1.metric('temp','234')
col2.metric('hum','2345')
col3.metric('weather','clear')

temp=st.number_input('Enter Temprature: ')
humidity=st.number_input('Enter humidity: ')
hour=st.slider('Hour?',0,24,16)
is_rush_hour=st.selectbox('Is Rush or Not? ',[1,0])
month=st.slider('Month?',1,12,10)
season_sele=st.selectbox('season? ',['winter','spring','summer','fall']) 
season=season_dummies[season_sele]
weather_sele=st.selectbox('weather? ',['clear','mist','rainy','snowy']) 
weather=weather_dummies[weather_sele]
weeek_day_sele=st.selectbox('week_day? ',['saturday','sunday','monday','tuesday','wednesday','thursday','friday'])
week_day=weekdays_dummies[weeek_day_sele]
pod_sele=st.selectbox('Period of day? ',['evening','morning','night','afternoon'])
pod=pod_dummies[pod_sele]

data=[temp,humidity,hour,is_rush_hour,month]
data=data+season+weather+week_day+pod

data_scaled=scaler.transform([data])

result=model.predict([data])

st.write(result)



