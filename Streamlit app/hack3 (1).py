#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import numpy as np
from page1 import page1


# Initialize session_state
if 'page' not in st.session_state:
    st.session_state.page = 1

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

if selected_page == "Page 1":
    st.session_state.page = 1
elif selected_page == "Page 2":
    st.session_state.page = 2

# Display the selected page
if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()


st.title('Space Exploration')

import streamlit as st

# Create a button to redirect to Page 2
if st.button("Go to Page 2"):
    st.session_state.page = 2  # Set the page number to 2

    
st.sidebar.header("Explore")
# User customization
st.sidebar.markdown("---")
user_name = st.sidebar.text_input("Your Name", "Anonymous")


# User Accounts
st.sidebar.markdown("---")
st.sidebar.header("User Accounts")
if st.sidebar.button("Create Account"):
    # Implement user account creation
    st.sidebar.text("Account created!")
if st.sidebar.button("Login"):
    # Implement user login
    st.sidebar.text("Logged in as user")
    
angle = st.sidebar.slider('Set launch angle', min_value=0, max_value=90, value=45)
power = st.slider.sidebar('Set launch power', min_value=10, max_value=100, value=50)

if st.button('Launch!'):
  launch_rocket(angle, power)
  st.balloons()
    

# Background Music Selection
st.sidebar.markdown("---")
st.sidebar.header("Background Music")
background_music = st.sidebar.selectbox("Background Music", ["None", "Space Ambient", "Epic Space", "Relaxing Space"])
if background_music != "None":
    st.audio(f"{background_music}.mp3")



st.header('Planets Data')

planets = pd.DataFrame({
  'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
  'Mass': [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102],
  'Diameter': [4879, 12104, 12742, 6792, 142984, 120536, 51118, 49528]  
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

st.write("""
This creates a simple space-themed site with:

- A planets data table 
- An interactive planet fact selector
- A rocket launch countdown timer
- Some astronaut images
        
You can customize it further by adding more pages, data, images etc.
""")


# In[ ]:




