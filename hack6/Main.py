import pymongo
import streamlit as st
from pymongo import MongoClient as mc
from datetime import date,datetime 
from PIL import Image
import base64

cluster = mc('mongodb+srv://ps332:ps332@cluster0.z5ipz8j.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp')
db = cluster["DB"]
collection = db["Data"]

st.set_page_config (page_title="Girl Hacks 2023", page_icon="📒",layout="wide")
# st.markdown(""" <style>#Sidebsr {visibility: hidden;}footer {visibility: hidden;}</style> """, unsafe_allow_html=True)

st.write('<style>div.block-container{padding-left:0 rem;padding-top:0.1rem;}</style>', unsafe_allow_html=True)

st.markdown("<h1 style='color:#66fcf1;text-align: center;'>Latest Space Events </h1>",unsafe_allow_html=True)
for i in range(1,3):
	st.write("")

INSERT,padding,ID1,DATE,NOTES,DELETE = st.columns((0.5,0.0000005,0.8,1.6,5,1))

with INSERT:
	st.sidebar.markdown("<h3 style='color:#66fcf1;text-align: center;'>Enter the event details</h3>",unsafe_allow_html=True)
	st.sidebar.write('')			   
	txt = st.sidebar.text_area("Enter event title")
	st.sidebar.write('')
	d = st.sidebar.date_input("Select a Date")
	dd = str(d)
	st.sidebar.write('')
	post = {"Date":dd, "Note":txt}
	if st.sidebar.button('→',key = 754789):
		collection.insert_one(post)
		st.experimental_rerun()
        


with DATE:
	st.markdown("<h4 style='color:#66fcf1;text-align: center;'>Date</h4>",unsafe_allow_html=True)
	st.write('')
	for record in collection.find({},{ "_id": 0,"Date":1 }):
		for v in record.values():              
			def header(v):                 
				st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#1f1833;text-align: center;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
			header(v)

with NOTES:
	st.markdown("<h4 style='color:#66fcf1;text-align: center;'>Event Title </h4>",unsafe_allow_html=True)
	st.write('')

	for record in collection.find({},{ "_id": 0,"Note":1 }):
		for v in record.values():              
			def header(v):                 
				st.markdown(f'<p style="border-style:solid;border-color:#66fcf1;background-color:#1f1833;text-align:center;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
			header(v)

with ID1:
	st.markdown("<h4 style='color:#66fcf1;text-align: center;'>No</h4>",unsafe_allow_html=True)
	st.write('')
	ass =  collection.count_documents({})
	ID = ass + 1
	for i in range(1,ID):
		st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#1f1833;text-align:center; padding:15px; color:white; font-size:20px; border-radius:8px">{i}</p>', unsafe_allow_html=True)

with DELETE:
	for i in range(1,6):
		st.write('')
	for record in collection.find({},{ "_id": 1}):
		for vv in record.values():
			if st.button("🗑",key=vv):
				delete = {"_id": vv}
				collection.delete_one(delete)
				st.experimental_rerun()			
			st.markdown("""<style>.stButton > button {border-style: solid;border-color:#66fcf1;color: white;margin:-2px;background: #1f1833;width: 40px;height: 50px;}</style>""", unsafe_allow_html=True)