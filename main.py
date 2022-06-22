import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import matplotlib.pyplot as plt


components.html('<html><body><h1 style="color:#1C1F2F;text-align: center;">Covid-19 Information in Asia</h1></body></html>')

#Loading dataset

covid_df=pd.read_csv('Covid.csv')
graph_df=pd.DataFrame({'graph':['Pie Chart','Bar Chart']})

st.sidebar.header('Select what to display')

#Selectbox

country_name=st.sidebar.selectbox('Choose country...',covid_df['Country'])

#Radio

graph_type = st.sidebar.radio("Choose graph type...",graph_df['graph'])

#Button

show_button=st.sidebar.button("Show Information")


asian = st.sidebar.checkbox('All Asian Countries Data')

if asian:
     st.table(covid_df)


if show_button:


	st.subheader(country_name)
	
	#For Country

	answer_df=covid_df.loc[covid_df["Country"] == country_name]
	

	col1_p,col2_p=st.columns([3,1])
	col1_p.success('Population')
	col2_p.success(int(answer_df['Population'].values))

	col1_c,col2_c=st.columns([3,1])
	col1_c.success('Total Confirmed Cases')
	col2_c.success(int(answer_df['Total Cases'].values))

	col1_d,col2_d=st.columns([3,1])
	col1_d.success('Total Deaths')
	col2_d.success(int(answer_df['Total Deaths'].values))

	col1_r,col2_r=st.columns([3,1])
	col1_r.success('Total Recovered')
	col2_r.success(int(answer_df['Total Recovered'].values))

	col1_a,col2_a=st.columns([3,1])
	col1_a.success('Active Cases')
	col2_a.success(int(answer_df['Active Cases'].values))

	
	# Plotting matplotlib

	case=int(answer_df['Total Cases'])
	death=int(answer_df['Total Deaths'])
	recovered=int(answer_df['Total Recovered'])
	active=int(answer_df['Active Cases'])

	labels = ["Total Cases", "Total Deaths","Total Recovered","Active Cases"]
	sizes=[case,death,recovered,active]

	if graph_type=='Pie Chart':

		st.subheader('Pie Chart')

		#---Pie Chart---

		fig, ax = plt.subplots(figsize=(6,6))
		ax.pie(sizes, labels=labels, autopct="%1.1f%%")
		ax.axis("equal")

		st.pyplot(fig)


	elif graph_type=='Bar Chart':

		st.subheader('Bar Chart')

		#---Bar Chart---

		data=[[case,death,recovered,active]]
		df = pd.DataFrame(data, columns=["Total Cases", "Total Deaths","Total Recovered","Active Cases"])
		st.bar_chart(df,width=1500, height=500)


	






	
	        


	