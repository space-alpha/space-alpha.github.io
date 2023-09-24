#!/usr/bin/env python
# coding: utf-8

# In[1]:


# page1.py

import streamlit as st

import pandas as pd
import numpy as np


def page1():
    st.title('Space Exploration')
    st.header('Planets Data')
    planets = pd.DataFrame({

        'Mercury': [0.330, 4879],
        'Venus': [4.87, 12104],
        'Earth': [5.97, 12742],
        'Mars': [0.642, 6792],
        'Jupiter': [1898, 142984],
        'Saturn': [568, 120536],
        'Uranus': [86.8, 51118],
        'Neptune': [102, 49528]
    })

    st.dataframe(planets)
    st.header('Planet Facts')
    planet_fact = st.selectbox('Select a planet to see a fact', 
                               ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'])

    if planet_fact == 'Mercury':
      st.write('Mercury has no natural satellites')  
    elif planet_fact == 'Venus':
      st.write("Venus is the hottest planet in the solar system")
    elif planet_fact == 'Earth':
      st.write("Earth is the only planet known to have life")
    elif planet_fact == 'Mars':
      st.write("Mars is known as the Red Planet")  
    elif planet_fact == 'Jupiter':
      st.write("Jupiter is the largest planet in the solar system")
    elif planet_fact == 'Saturn':
      st.write("Saturn has prominent rings around it")
    elif planet_fact == 'Uranus':
      st.write("Uranus rotates on its side compared to the other planets")
    elif planet_fact == 'Neptune':
      st.write("Neptune was the first planet located through mathematical predictions rather than observation")
    #new 
     #new end
    st.header('Rocket Launch Countdown')

    launch_time = st.number_input('Enter launch time (in seconds):', min_value=10, max_value=100, value=10)

    if st.button('Launch!'):
      for i in range(launch_time, 0, -1):
        st.write(i)
      st.balloons()

    st.header('Astronaut Image Gallery')

    col1, col2 = st.columns(2)

    with col1:
      st.image("astronaut1.jpeg")
    with col2:  
      st.image("astronaut2.jpeg")
    
    st.image("astronaut3.webp")
    st.image("astronaut4.jpg")
    st.image("astronaut5.jpg")


# In[ ]:




