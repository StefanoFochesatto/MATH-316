#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import plotly.express as px #Plotly libraries
import plotly.graph_objects as go
import plotly.express as px

from jupyter_plotly_dash import JupyterDash #Dash for Jupyter Library
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# In[2]:


#Initial Data Wrangle
wtr = pd.read_csv('weatherAUS.csv')
wtr['Year'] = wtr['Date'].str.slice(2, 4).astype(int) 
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
wtr.head()

#Inputs for mean variable and time series interval
min = 8
max = 10
location = 'Melbourne'
datatype = 'Rainfall'


#Intermediate dataframe wrangle
df = wtr[(wtr['Location'] == location) & ((wtr['Year'] >= min)&(wtr['Year'] <= max))]


#Calculating the mean variable, and assigning month and year data.
mean_variable = []
for j in range(max-min+1):
    for i in range(12):
        mean_variable.append(df[(df['Date'].str.slice(5, 7).astype(int) == i+1) & (df['Year'] == (j+min))][datatype].mean())


index = []
for i in range(max-min+1):
    index = np.append(index,months)
    
    
    
years = []
for i in range(max-min+1):
    years = np.append(years,np.ones(12)*(i + min)).astype(str) 

    
    
#Dataframe set for PlotlyExpress Library
d = {'mean':mean_variable, 'Month':index, 'Years':years}
df = pd.DataFrame(data = d)
df.head()


#Result Example
fig_barpolar = px.bar_polar(df, r="mean", theta="Month", color="Years",template="ggplot2", barmode='overlay',title="Monthly Mean "+datatype+" in "+location)
fig_barpolar.show()




# In[3]:


#Initial Data Wrangle
md = pd.read_csv('MonthlyDeaths.csv')
md.head()

#Inputs for mean variable and time series interval
min = 2018
max = 2020




#Intermediate dataframe wrangle
df_m = md[(md['Year_of_Death'] >= min)&(md['Year_of_Death'] <= max)]

#Dataframe set for PlotlyExpress Library
d_m = {'Total':df_m['Deaths'], 'Month':df_m['Month_Text'], 'Year':df_m['Year_of_Death'].astype(str)}
df_m = pd.DataFrame(data = d_m)
df_m.head()

fig_barpolar_m = px.bar_polar(df_m, r="Total", theta="Month", color="Year" ,template="ggplot2", barmode='overlay',color_discrete_sequence= px.colors.sequential.Plasma_r)
fig_barpolar_m.show()

fig_m = px.line_polar(df_m, r="Total", theta="Month", color="Year", line_close=True, template="ggplot2",color_discrete_sequence= px.colors.sequential.Plasma_r)
fig_m.update_traces(fill='toself')


# In[4]:


df_w = px.data.wind()



fig = px.bar_polar(df_w, r="frequency", theta="direction", color="strength", template="ggplot2", color_discrete_sequence= px.colors.sequential.Plasma_r, title = 'Wind Data Example')
fig.show()

fig = px.line_polar(df_w, r="frequency", theta="direction", color="strength", template="ggplot2", color_discrete_sequence= px.colors.sequential.Plasma_r, line_close = True, title = 'Wind Data Example')
fig.update_traces(fill='toself')
fig.show()


# In[5]:


app = JupyterDash('example')

colors = {
    'background': '#00000',
    'text': '#FFFFF'
}


app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    
    dcc.Graph(
        id='graph',
        figure=fig_barpolar,
        style={'width': '80%', 'height': '80%',
            "display": "inline-block",
            "overflow": "hidden",
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)"
        }
    ),
    
    
    
    html.H1(
        children='Florence Nightingale Diagram',
                style={
            'font-family':'Helvetica',
            'textAlign': 'left',
            'padding-left': '8%',
            "position": "relative",
            'padding-top': '2%',
            'color': colors['text']
        }
    ),

    
    
    
    html.H2(children='Visualizing Data', style={
        'font-family':'Helvetica',
        'textAlign': 'left',
        "position": "relative",
        'padding-left': '10%',
        'color': colors['text']
    }),
    
    
        dcc.RadioItems(
        id='Style', 
        value='Polar-Area', 
        options=[{'value': x, 'label': x} 
                 for x in ['Polar-Area', 'Scatter-Polar']],
         style={
            'font-family':'Helvetica',
            "display": "inline-block",
            "overflow": "hidden",
            "position": "absolute",
            "top": "85%",
            "left": "20%",
            "transform": "translate(-50%, -50%)",
            'color': colors['text']
        }
    
    ),
    
    
       dcc.RadioItems(
        id='DataExample', 
        value='button', 
        options=[{'value': x, 'label': x} 
                 for x in ['Australia Weather', 'Michigan COVID', 'Windspeed Data']],
         style={
            'font-family':'Helvetica',
            "display": "inline-block",
            "overflow": "hidden",
            "position": "absolute",
            "top": "75%",
            "left": "20%",
            "transform": "translate(-50%, -50%)",
            'color': colors['text']
        }
    
    )
    

])












@app.callback(
    Output("graph", "figure"), 
    Input("Style", "value"),
    Input("DataExample", "value"))

def generate_chart(Style, DataExample):

    if DataExample == 'Australia Weather':
        if Style == 'Polar-Area':
            fig = px.bar_polar(df, r="mean", theta="Month", color="Years",template="ggplot2",title="Monthly Mean "+datatype+" in "+location,color_discrete_sequence= px.colors.sequential.Plasma_r)
        else:
            fig = px.line_polar(df, r="mean", theta="Month", color="Years", line_close=True, template="ggplot2",title="Monthly Mean "+datatype+" in "+location,color_discrete_sequence= px.colors.sequential.Plasma_r)
            fig.update_traces(fill='toself')
        return fig

    elif DataExample == 'Michigan COVID': 
        if Style == 'Polar-Area':
            fig = px.bar_polar(df_m, r="Total", theta="Month", color="Year" ,template="ggplot2", barmode='overlay',title="Monthly Mean Deaths in Michigan",color_discrete_sequence= px.colors.sequential.Plasma_r)
        else:
            fig = px.line_polar(df_m, r="Total", theta="Month", color="Year", line_close=True, template="ggplot2",title="Monthly Mean Deaths in Michigan",color_discrete_sequence= px.colors.sequential.Plasma_r)
            fig.update_traces(fill='toself')
        return fig
        
    else: 
        if Style == 'Polar-Area':
            fig = px.bar_polar(df_w, r="frequency", theta="direction", color="strength", template="ggplot2", color_discrete_sequence= px.colors.sequential.Plasma_r, title = 'Wind Data Example')
        else:
            fig = px.line_polar(df_w, r="frequency", theta="direction", color="strength", template="ggplot2", color_discrete_sequence= px.colors.sequential.Plasma_r, line_close = True, title = 'Wind Data Example')
            fig.update_traces(fill='toself')
        return fig
        



app


# In[ ]:





# In[ ]:





# In[6]:


#Initial Data Wrangle
md = pd.read_csv('MonthlyDeaths.csv')
md.head()

#Inputs for mean variable and time series interval
min = 2018
max = 2020
datatype = 'Deaths'



#Intermediate dataframe wrangle
df = md[(md['Year_of_Death'] >= min)&(md['Year_of_Death'] <= max)]

#Dataframe set for PlotlyExpress Library
d = {'Total':df['Deaths'], 'Month':df['Month_Text'], 'Year':df['Year_of_Death'].astype(str)}
df = pd.DataFrame(data = d)
df.head()

fig_barpolar = px.bar_polar(df, r="Total", theta="Month", color="Year" ,template="ggplot2", barmode='overlay')
fig_barpolar.show()

fig = px.line_polar(df, r="Total", theta="Month", color="Year", line_close=True, template="ggplot2")
fig.update_traces(fill='toself')


# In[7]:


import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()


# In[8]:


df = px.data.wind()
fig = px.bar(df, x="frequency", y="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r, barmode = 'overlay')
fig.show()


# In[ ]:




