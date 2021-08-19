import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
from plotly.subplots import make_subplots


password= st.text_input('Please Enter The Password')
if password == "fis@2021":
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file1.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past few months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],0,total_selections.values[1,1],total_selections.values[0,0]))
	#st.write('\n\n As can be seen, out of %s total selections: \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted and \n\n %s Candidates are yet to join '%(total_selections1.values[0],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for two levels, **Junior Level** for Offered CTC < 15 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'])
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'])
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,2],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'])
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[1,4], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[1,4], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,0], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],0))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)



if password== 'navi@2021':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file2.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	



	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July  2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past 4 Months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")
	
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[1,1],0,total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)
	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** different skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)



	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,2], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,1], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
	



if password== 'bottomline@2020':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file3.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	



	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past few months ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Joining Pending")
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Joining Pending')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are yet to join '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[0,0],total_selections.values[1,1]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)

	



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))
	
	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	

	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,3], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,1], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	
	
	
	



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)



if password== 'britishtelecom@2020':


	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)
	
	DATA_URL= 'file4.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()
	
	

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past year ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(status_count)

	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s Candidates were Offered \n\n %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidates are yet to join '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[0,0],total_selections.values[1,1]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	#st.write(level_conversion1)
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s.'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],level_conversion.values[1,1],level_conversion.values[2,2]))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection of a submitted candidate. \n\n**%s** days was the maximum number of days taken for the same \n\n **%s** days was the minimum number of days that was taken for a selection of a submitted candidate"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[29,75], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[22,48], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[4,9],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)






	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)


if password== 'datacore@2020':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file5.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past year ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Joinings")
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Joining Pending')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidates are yet to join. '%(total_selections1.values[0],offer_count.values[1],total_selections.values[1,1],total_selections.values[0,0],0))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	#st.write(level_conversion1)
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[29,75], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[22,48], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[4,9],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)




	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)


if password== 'delhivery@2020':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file6.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past year ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Joinings")
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Joining Pending')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidates are yet to join. '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	#st.write(level_conversion1)
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],level_conversion.values[1,1],0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,7], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,5], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	pending=data.groupby(['Status']).count()
	pending=pending.values[1,1]
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	#st.write(pending)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[2,2]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)


if password== 'deloitte@2020':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file7.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the Past 4 Months')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions and Pending Joinings")
	
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)
	#st.write(total_selections1)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Pending Joinings')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidates are yet to Join '%(total_selections1.values[0],offer_count.values[1],total_selections.values[0,0],0,0))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.scatter(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[0,0],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[5,6], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[3,1], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[3,1],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	#pending=data.groupby(['Status']).count()
	#pending=pending.values[1,1]
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	#st.write(pending)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[0,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)


if password== 'grantthornton@2020':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file8.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past year ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Conversions")
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Pending Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[1,1],total_selections.values[0,0],0))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,7], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,3], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	pending=data.groupby(['Status']).count()
	pending=pending.values[1,1]
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	#st.write(pending)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,1]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions for FY 2020-21. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)



if password== 'guardian@2021':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'guardian.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past 4 months ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Joining")
	
		#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Pending Joining')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],level_conversion.values[1,1],0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[2,2],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[4,25], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[2,19], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,7],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	pending=data.groupby(['Status']).count()
	pending=pending.values[1,1]
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining TAT'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	#st.write(pending)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,1]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)


if password== 'airtelpaymentsbank@2020':
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file10.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past 4 Months')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Joining")
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Pending Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[0,0],total_selections.values[1,1]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0] ))
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,7], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,3], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2],name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	pending=data.groupby(['Status']).count()
	pending=pending.values[1,1]
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	#st.write(pending)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,1]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	

	




	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
	
if password == "dailyhunt@2021":
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'dailyhunt.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past few months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],0,total_selections.values[0,0],0))

	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for two levels, **Junior Level** for Offered CTC < 15 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'])
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'])
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	#st.sidebar.markdown('### Joining TAT')

	#joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	#joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	#st.markdown('### Joining TAT')
	#st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	#st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,2],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	#if st.sidebar.checkbox('Visual',True,key=5):
	#	fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'])
	#	fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
	#	fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
	#	st.plotly_chart(fig5)

	#st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,6], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,4], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,4], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],0))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
	
if password == "nxp@2021":
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'nxp.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past few months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	#st.write('\n\n As can be seen, out of %s total selections: \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted and \n\n %s Candidates are yet to join '%(total_selections1.values[0],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for two levels, **Junior Level** for Offered CTC < 15 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'])
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'])
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,2],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'])
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[0,7], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[0,4], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[0,2], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],0))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
	
if password== 'protiviti@2021':

	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'protiviti.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	



	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July  2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past 4 Months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")
	
	
	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[1,1],total_selections.values[0,0],0))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)
	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** different skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.scatter(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)



	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'],height=600)
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'],height=500)
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	#st.sidebar.markdown('### Joining TAT')

	#joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	
	#joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	#st.markdown('### Joining TAT')
	#st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	#st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,1],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	#if st.sidebar.checkbox('Visual',True,key=5):
	#	fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'],height=500)
	#	fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
	#	fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
	#	st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[3,5], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[3,2], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[2,1], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],total_selections.values[1,0]))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)
	



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
	
if password == "s&p@2021":
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 's&p.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	total_selections=data['Status'].value_counts()
	total_selections=data.groupby('Status').count()


	total_selections1=data['Client'].value_counts()
	total_selections1=data.groupby('Client').count()
	total_selections1=total_selections1.sum()
	#st.write(total_selections1)
	#st.write(total_selections)

	
	

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report April-July 2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past few months ')

	st.sidebar.markdown("### Number Of Positive Coneversions and Negative Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})
	offer_count=data['Offer Date'].value_counts()
	offer_count=data.groupby('Offer Date').count()
	offer_count=offer_count.sum()
	#st.write(offer_count)


	st.markdown('### Number Of Positive Conversions and Negative Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of %s total selections:\n\n %s candidates were offered \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted \n\n %s Candidate Conversions are still Pending '%(total_selections1.values[0],offer_count.values[1],total_selections.values[1,1],0,total_selections.values[0,0]))
	#st.write('\n\n As can be seen, out of %s total selections: \n\n Out of which, %s Candidates were Positively Converted \n\n %s Candidates were not Converted and \n\n %s Candidates are yet to join '%(total_selections1.values[0],total_selections.values[2,2],total_selections.values[1,1],total_selections.values[0,0]))
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")

	skill = data['Skill'].value_counts()
	skill=data.groupby('Skill').count()
	skill=skill.sum()
	#st.write(skill)

	level_conversion=data.groupby('Level').count()
	#st.write(level_conversion)



	level_roles = data['Level'].value_counts()
	level_conversion1=data.groupby('Level').count()
	level_conversion1=level_conversion1.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion1.values })
	#st.write(level_roles)
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **%s** skills and roles for %s. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill'%(skill.values[0],clients.index[0]) )
	st.write('Hiring was done for two levels, **Junior Level** for Offered CTC < 15 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **%s** Selections were done for the Junior Level roles. \n\n **%s** Selections were done for the Middle Level Roles. \n\n **%s** Selections were done for Senior Level roles'%(level_conversion.values[0,0],0,0))
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.scatter(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by %s to select a submitted candidate"%(clients.index[0]))
	st.write("**%s** Days were taken on an average for a selection. \n\n**%s** days was the maximum number of days that was taken for a selection \n\n **%s** days was the minimum number of days that was taken for a selection"%(selection_tat_count.values[0,1],selection_tat_count.values[2,1],selection_tat_count.values[1,1]))
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'])
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert a selection to Offer"%(clients.index[0]))
	st.write("**%s** Days were taken on an average to convert a selection to an offer. \n\n Maximum **%s** Days were taken for the same. \n\n Minimum **%s** Days were taken"%(offer_tat_count.values[0,1],offer_tat_count.values[2,1],offer_tat_count.values[1,1]))

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'])
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	#st.write(joining_tat_count)
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by %s to convert the status of a candidate from Offer to Joining"%(clients.index[0]))
	st.write("**%s** Positive Conversions took place,\n\n **%s** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**%s** Days were the minimum number of days taken for the same \n\n **%s** days were the maximum number of days taken for a joining."%(total_selections.values[1,2],joining_tat_count.values[0,1],joining_tat_count.values[1,1],joining_tat_count.values[2,1]))
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'])
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)

	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		value_list1= data['Skill'].to_list()
		value_list1 = [x for x in value_list1 if pd.isnull(x) == False and x != 'nan']
		value_list2=data['Role'].to_list()
		value_list2= [x for x in value_list2 if pd.isnull(x) == False and x != 'nan']
		value_list=value_list1+value_list2
		words=(','.join(str(v) for v in value_list))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for %s'%clients.index[0])
	
	st.write("***Diversity Ratio***")

	st.write("The figure depicts the diversity percentage in all the three stages from selection to joining of candidates.")
	labels=['Female','Male']
	gender_data=data.groupby('Gender').count()
	#st.write(gender_data)
	
	fig10 = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
	fig10.add_trace(go.Pie(labels=labels, values=[5,6], name="Selected Candidates Diversity Percentage"),1, 1)
	fig10.add_trace(go.Pie(labels=labels, values=[4,6], name="Offered Candidates Diversity Percentage"),1, 2)
	fig10.add_trace(go.Pie(labels=labels, values=[4,4], name="Joined Candidates Diversity Percentage"),1, 3)

	fig10.update_traces(hole=.4, hoverinfo="label+percent+name")
	fig10.update_layout(title_text="Diversity Percentage for all three stages",annotations=[dict(text='Selections', x=0.09, y=0.5, font_size=12, showarrow=False),
                 dict(text='Offered', x=0.50, y=0.5, font_size=12, showarrow=False),dict(text='Joined', x=0.90, y=0.5, font_size=12, showarrow=False)])
	st.plotly_chart(fig10)

	st.write("***Throughput ratios***")
	total_submissions=data['Submission Date'].count()
	selections=data['Selection Date'].count()
	offers=data['Offer Date'].count()
	joinings=data['Joining Date'].count()
	offer_percent=round(offers/selections*100)
	joining_percent=round(joinings/offers*100)
	st.write("As can be seen, out of total %s Selections, %s Candidates Joined"%(total_selections1.values[0],0))
	st.write("There was a "+str(offer_percent)+"% Selection Conversion and "+str(joining_percent)+"% Offer Conversion")
	df=pd.DataFrame({'Stage':['Selections','Offers','Joining'],'Number':[[selections],[offers],[joinings]]})
#	st.write(df)
	#df7=pd.DataFrame({'Stage':['Selections','Joining'],'Number':[[total_selections1.values[0],[total_selections.values[1,0]]]})
	fi7=px.funnel(df,y='Stage',x=[selections,offers,joinings],labels='Number of Candidates')
	#fig7=px.funnel(df7,x='Stage',y='Number',labels='Number of Candidates')
	st.plotly_chart(fi7)




	st.write("Hiring was done for the Highlighted Locations")
	lat=data['lat']
	lon=data['lon']
	map=pd.DataFrame({'lat':lat.values,'lon':lon.values})

	#st.write(map)
	st.map(map)



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)

	
	





else:
	st.write('Please Enter The Correct Password')
