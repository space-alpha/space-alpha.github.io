#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import pandas as pd
import numpy as np
from page1 import page1
from page2 import page2

# Initialize session_state
if 'page' not in st.session_state:
    st.session_state.page = 1

# Sidebar navigation

if st.sidebar.button("Page 1"):
    st.session_state.page = 1
if st.sidebar.button("Page 2"):
    st.session_state.page = 2

# Display the selected page
if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()


# In[ ]:





# In[ ]:




