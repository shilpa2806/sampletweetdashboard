import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt
import tweepy
from langdetect import detect
from PIL import Image
import tweepy
import re
from time import time, sleep
import time
import datetime
import base64

assemblies = ["Ichchapuram",
"Palakonda",
"Gurazala",
"Macherla",
"Yerragondapalem",
"Darsi",
"Parchur",
"Addanki",
"Chirala",
"Santhanuthalapadu",
"Ongole",
"Kandukur",
"Kurupam",
"Kondapi",
"Markapuram",
"Giddalur",
"Kanigiri",
"Kavali",
"Atmakur",
"Kovur",
"Nellore City",
"Nellore Rural",
"Sarvepalli",
"Parvathipuram",
"Gudur",
"Sullurpeta",
"Venkatagiri",
"Udayagiri",
"Badvel",
"Rajampet",
"Kadapa",
"Kodur",
"Rayachoti",
"Pulivendla",
"Salur",
"Kamalapuram",
"Jammalamadugu",
"Proddatur",
"Mydukur",
"Allagadda",
"Srisailam",
"Nandikotkur",
"Kurnool",
"Panyam",
"Nandyal",
"Bobbili",
"Banaganapalle",
"Dhone",
"Pattikonda",
"Kodumur",
"Yemmiganur",
"Mantralayam",
"Adoni",
"Alur",
"Rayadurg",
"Uravakonda",
"Cheepurupalle",
"Guntakal",
"Tadipatri",
"Singanamala",
"Anantapur urban",
"KALYANDURG",
"Raptadu",
"Madakasira",
"Hindupur",
"Penukonda",
"Puttaparthi",
"Gajapathinagaram",
"Dharmavaram",
"Kadiri",
"Thamballapalle",
"Pileru",
"Madanapalle",
"Punganur",
"Chandragiri",
"Tirupati",
"Srikalahasti",
"Satyavedu",
"Nellimarla",
"Nagari",
"Gangadhara Nellore",
"Chittoor",
"Puthalapattu",
"Palamaner",
"Kuppam",
"Vizianagaram",
"Srungavarapukota",
"Palasa",
"Bhimli",
"Visakhapatnam East",
"Visakhapatnam South",
"Visakhapatnam North",
"Visakhapatnam West",
"Gajuwaka",
"Chodavaram",
"V.Madugula",
"Araku valley",
"Paderu",
"Tekkali",
"Anakapalli",
"Pendurthi",
"Yelamanchili",
"Payakaraopet",
"Narsipatnam",
"Tuni",
"Prathipadu",
"Pithapuram",
"Kakinada Rural",
"Peddapuram",
"Pathapatnam",
"Anaparthy",
"Kakinada City",
"Ramachandrapuram",
"Mummidivaram",
"Amalapuram",
"Razole",
"Gannavaram",
"Kothapeta",
"Mandapeta",
"Rajanagaram",
"Srikakulam",
"Rajahmundry City",
"Rajamundry Rural",
"Jaggampeta",
"Rampachodavaram",
"Kovvur",
"Nidadavole",
"Achanta",
"Palacole",
"Narasapuram",
"Bhimavaram",
"Amadalavalasa",
"Undi",
"TANUKU",
"Tadepalligudem",
"Unguturu",
"Denduluru",
"Eluru",
"Gopalapuram",
"Polavaram",
"Chintalapudi",
"Tiruvuru",
"Etcherla",
"Nuzvid",
"Gannavaram",
"Gudivada",
"Kaikalur",
"Pedana",
"Machilipatnam",
"Avanigadda",
"Pamarru",
"Penamaluru",
"Vijaywada West",
"Narasannapeta",
"Vijayawada central",
"Vijayawada East",
"Mylavaram",
"Nandigama",
"Jaggayyapeta",
"Pedakurapadu",
"Tadikonda",
"Mangalagiri",
"Ponnur",
"Vemuru",
"Rajam",
"Repalle",
"Tenali",
"Bapatla",
"Prathipadu",
"Guntur West",
"Guntur East",
"Chilakaluripet",
"Narasaraopet",
"Sattenpalli",
"Vinukonda",
]    



keyowrd = "janasenaparty"
im = Image.open("icon.ico")
st.set_page_config(
    page_title="JSP Social Media Dashboard",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="collapsed"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0.5rem;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




BACKGROUND_COLOR = 'red'
COLOR = 'black'

def set_page_container_style(
        max_width: int = 1100, max_width_100_percent: bool = False,
        padding_top: int = 1, padding_right: int = 10, padding_left: int = 1, padding_bottom: int = 10,
        color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
        if max_width_100_percent:
            max_width_str = f'max-width: 100%;'
        else:
            max_width_str = f'max-width: {max_width}px;'
        st.markdown(
            f'''
            <style>
                .reportview-container .css-1lcbmhc .css-1outpf7 {{
                    padding-top: 35px;
                }}
                .reportview-container .main .block-container {{
                    {max_width_str}
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
                .reportview-container .main {{
                    color: {color};
                    background-color: {background_color};
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )









set_page_container_style(
        max_width = 1100, max_width_100_percent = True,
        padding_top = 0, padding_right = 0, padding_left = 5, padding_bottom = 0, background_color = "green"
)



with st.sidebar:

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ce1126;
        color: white;
        height: 3em;
        width: 12em;
        border-radius:10px;
        border:3px solid #000000;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
    }
    
    div.stButton > button:hover {
        background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
        background-color:#ce1126;
    }
    
    div.stButton > button:active {
        background:linear-gradient(to bottom, #063B01 1%, #10C801 100%);
        background-color:#063B01;
        position:relative;
        top:1px;
    }
    
    </style>""", unsafe_allow_html=True)
    dashboard = st.button("Dashboard")
    
    
    st.markdown('<p></p>', unsafe_allow_html = True)
    constituencydb = st.selectbox('Select Constituency', sorted(assemblies), key="1")
    st.markdown('<p></p>', unsafe_allow_html = True)
    st.markdown('<p></p>', unsafe_allow_html = True)
    
    leaderboard = st .button("Leaderboard")
    
    st.markdown('<p></p>', unsafe_allow_html = True)
    constituencylb = st.selectbox('Select Constituency', sorted(assemblies), key="2")
    st.markdown('<p></p>', unsafe_allow_html = True)
    st.markdown('<p></p>', unsafe_allow_html = True)
    
    reqideas = st .button("Requirements/ Ideas")
    
    st.markdown('<p></p>', unsafe_allow_html = True)
    st.markdown('<p></p>', unsafe_allow_html = True)
    st.markdown('<p></p>', unsafe_allow_html = True)
     
    reqideas = st .button("Bugs/ Feedback")
col1, col2, col3 = st.columns(3)    
with col1:
    st.image("emblem_only.png", width=300, use_column_width=None)
with col3: 
    st.markdown("<p style='text-align: center; color: #970404;'><b>Tweets today</b></p>", unsafe_allow_html=True)
url = "janasena_citywise.csv"
df_assembly = pd.read_csv(url)
df_assembly[['latitude', 'longitude']] = df_assembly['coords'].str.split(',', n=1, expand=True)

url = "janasena_all_tweets.csv"
df_all = pd.read_csv(url)
df_all_filtered = df_all[df_all.Username != "JanaSenaParty"]
df_all_Janasenaparty = df_all[df_all.Username == "JanaSenaParty"]
#userdf = df_all.drop_duplicates(subset=['Username'])
#TotalReach = userdf['followers'].sum()  
url = "janasena_all_tweets_inclretweets.csv"
df_reach = pd.read_csv(url)
userdf = df_reach.drop_duplicates(subset=['Username'])
TotalReach = userdf['followers'].sum()  


def human_format(num):
    num = float('{:.4g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'Million', 'Billion', 'Trillion'][magnitude])
     
    
TotalReach_humanreadable = human_format(TotalReach)




#convert time column to a list, sort it and get count time wise
#df_all['Date'] = df_all['Date'].apply(lambda x: sorted(literal_eval(x)))
uniquetweetlist = df_all['Date'].values.tolist()
uniquetweetlist.sort()
count = 0
countlist = []
adjusted_timezone = []
for element in uniquetweetlist:
    clean_timestamp = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S%z')
    local_timestamp = clean_timestamp + datetime.timedelta(hours=5.5)
    final_timestamp = datetime.datetime.strftime(local_timestamp, '%Y-%m-%d %H:%M:%S%z')
    count += 1
    adjusted_timezone.append(final_timestamp)
    countlist.append(count)

#count likes, retweets and replies        
TotalRetweets = df_all['Likes'].sum()
TotalLikes = df_all['retweets'].sum()      
TotalReplies = df_all['replies'].sum()  
TotalTweets = TotalRetweets+count+TotalReplies
#TotalReach = TotalRetweets+count+TotalReplies + TotalLikes
Count_accounts = df_all['Username'].nunique()
totinklreplies = int(count+TotalReplies)


#sort tweets by likes and replies from Janasenaparty

popularbylikes_jsp_df_sorted = df_all_Janasenaparty.sort_values(by=['Likes'], ascending=False)
jspuniquetweetlist = popularbylikes_jsp_df_sorted['Date'].values.tolist()
jspadjusted_timezone = []
for element in jspuniquetweetlist:
    jspclean_timestamp = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S%z')
    jsplocal_timestamp = jspclean_timestamp + datetime.timedelta(hours=5.5)
    jspfinal_timestamp = datetime.datetime.strftime(jsplocal_timestamp, '%Y-%m-%d %H:%M:%S%z')
    jspadjusted_timezone.append(jspfinal_timestamp)
popularbylikes_jsp_df_sorted['date'] = jspadjusted_timezone
popularbylikes_jsp_df_sorted['date'] = popularbylikes_jsp_df_sorted['date'].str.slice(0,16)
popularbylikes_jsp_df = popularbylikes_jsp_df_sorted[['Username', 'Tweet', 'Likes', 'retweets', 'replies', 'date']]
#popularbyretweets_jsp_df = df_all_Janasenaparty.sort_values(by=['retweets'], ascending=False)

#sort tweets by likes and replies
popularbylikes_df = df_all_filtered.sort_values(by=['Likes'], ascending=False)
popularbyretweets_df = df_all_filtered.sort_values(by=['retweets'], ascending=False)

#create new dataframe only with tweets and usernames
popularbylikes_df_new = popularbylikes_df[['Username', 'Tweet', 'Likes']]
popularbyretweets_df_new = popularbyretweets_df[['Username', 'Tweet', 'retweets']]



fig_accounts = go.Figure(data=[go.Table(header=dict(values=['<b>Total Accounts</b>'], line_color='darkslategray',
    fill_color='red',
    align=['center'],
    font=dict(color='white', size=16),
    height=40),
                 cells=dict(values=[Count_accounts], line_color='darkslategray',
    fill_color='white',
    align=['center'],
    font=dict(color='black', size=16),
    height=40))
                     ])
                     
                     

fig_potential_reach = go.Figure(data=[go.Table(header=dict(values=['<b>Potential_reach</b>'], line_color='darkslategray',
    fill_color='red',
    align=['center'],
    font=dict(color='white', size=16),
    height=40),
                 cells=dict(values=[str(TotalReach_humanreadable)], line_color='darkslategray',
    fill_color='white',
    align=['center'],
    font=dict(color='black', size=20),
    height=40))
                     ])          




fig_total_tweets = go.Figure(data=[go.Table(header=dict(values=['<b>Total Unique Tweets</b>'], line_color='darkslategray',
    fill_color='red',
    align=['center'],
    font=dict(color='white', size=16),
    height=20),
                 cells=dict(values=[int(count)], line_color='darkslategray',
    fill_color='white',
    align=['center'],
    font=dict(color='black', size=16),
    height=40))
                     ])      




#col1, col2, col3, col4 = st.columns(4)
#
#with col1:
#
#    st.plotly_chart(fig_accounts, use_container_width=True)
#
#
#with col2:
#
#    st.plotly_chart(fig_potential_reach, use_container_width=True)
#
#with col3:
#
#    st.plotly_chart(fig_total_tweets, use_container_width=True)
#
#


#piechart






labels = ['Likes', 'Retweets', 'Replies' ]
values = [str(TotalLikes), str(TotalRetweets), str(TotalReplies)]
fig9 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0)])
#fig9.update_traces(textinfo=values)
fig9.update_traces(hoverinfo='label+percent', textinfo='label + value', textfont_size=15)
fig9.update_layout(showlegend=False, autosize=False,
    width=250, height=250, margin=dict(r=0, l=0, t=0, b=0))

#st.plotly_chart(fig9)

   






df_assembly['placetemp'] = df_assembly['place']
df_assembly1 = pd.DataFrame()
df_assembly2 = pd.DataFrame()

df_assembly1 = df_assembly["place"].value_counts().rename_axis('citycount').reset_index(name='counts')
df_assembly2 = df_assembly.groupby('placetemp').nth(0)

df_assembly2['tweetcount'] = df_assembly["placetemp"].value_counts()
df_assembly2 = df_assembly2.sort_values(by=['tweetcount'], ascending=False)
df_assembly2['tweetcount'].fillna(default_size, inplace=True) 

df_assembly3 = df_all.groupby('Username').nth(0)
df_assembly3['tweetcount'] = df_all['Username'].value_counts()
df_assembly3 = df_assembly3.sort_values(by=['tweetcount'], ascending=False)
df_assembly3 = df_assembly3.reset_index()
#df_assembly3_filtered = df_all[df_all.Username != "JanaSenaParty"]

#print(df_assembly3.head(10))




#df_assembly2.to_csv('test.csv')
#print(df_assembly2.head(50))
#print(df_assembly["place"].value_counts().head(50))
    
fig_city1 = px.density_mapbox(df_assembly2, lat='latitude', lon='longitude', radius=10,hover_name="place", hover_data=['tweetcount'],
                        center=dict(lat=16, lon=80), zoom=4,
                        mapbox_style="open-street-map")
                        
fig_city2 = px.scatter_mapbox(df_assembly2, lat="latitude", lon="longitude", hover_name="place", hover_data=['tweetcount'],
                        color_discrete_sequence=["fuchsia"], center=dict(lat=18, lon=85), zoom=5)
fig_city2.update_layout(mapbox_style="open-street-map")
fig_city2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

fig_city3 = px.scatter_geo(df_assembly2, lat="latitude", lon="longitude", color="tweetcount",
                     hover_name="place", size="tweetcount",
                     projection="natural earth2")
df_assembly2.drop_duplicates(subset="tweetcount",keep=False, inplace=True)
df_assembly2.sort_values("tweetcount", inplace=True, ascending=False)
fig_city4 = px.bar(df_assembly2.head(5), y='place', x='tweetcount',color="tweetcount", color_continuous_scale=px.colors.sequential.Rainbow, orientation='h')
fig_city4.update_yaxes(autorange="reversed")


#st.markdown('####') 
#st.markdown("<h1 style='text-align: center; color: #970404;'>TOP 10 By Tweet Counts</h1>", unsafe_allow_html=True) 
col1, col2, col3 = st.columns(3)
#print(df_assembly2.head(10))
df_topassemblies = df_assembly2[['place']]
#print(df_topassemblies.head(10))

fig15 = go.Figure(data=[go.Table(
    header=dict(values=list(df_topassemblies),
                fill_color='red',
                font=dict(color='white', family="Lato", size=20),
                align='center'),
    cells=dict(values=[df_topassemblies.place.head(10)],
               font=dict(color='black', family="Lato", size=10),
               fill_color='white',
               align='center'))
])



#TopTweeters
toptweeterlist = df_assembly3['Username'].tolist()
toptweetertcounts = df_assembly3['tweetcount'].tolist()


figtoptweeters = go.Figure()

figtoptweeters.add_trace(go.Indicator(
    value = toptweetertcounts[0], title = dict(
        text=toptweeterlist[0],
        font=dict(
            family="Arial",
            size=15,
            color='#040897'
        )),
    gauge = {
        'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
    domain = {'row': 0, 'column': 0}))
figtoptweeters.add_trace(go.Indicator(
    value = toptweetertcounts[1], title = dict(
        text=toptweeterlist[1],
        font=dict(
            family="Arial",
            size=15,
            color='#7F0D04'
        )),
    gauge = {
        'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
    domain = {'row': 0, 'column': 1}))
    
figtoptweeters.add_trace(go.Indicator(
   value = toptweetertcounts[2], title = dict(
        text=toptweeterlist[2],
        font=dict(
            family="Arial",
            size=15,
            color='#040897'
        )),
   gauge = {
       'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
   domain = {'row': 0, 'column': 2}))
   
figtoptweeters.add_trace(go.Indicator(
   value = toptweetertcounts[3], title = dict(
        text=toptweeterlist[3],
        font=dict(
            family="Arial",
            size=15,
            color='#040897'
        )),
   gauge = {
       'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
   domain = {'row': 1, 'column': 0}))
   
figtoptweeters.add_trace(go.Indicator(
   value = toptweetertcounts[4], title = dict(
        text=toptweeterlist[4],
        font=dict(
            family="Arial",
            size=15,
            color='#7F0D04'
        )),
   gauge = {
       'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
   domain = {'row': 1, 'column': 1}))
   
figtoptweeters.add_trace(go.Indicator(
   value = toptweetertcounts[5], title = dict(
        text=toptweeterlist[5],
        font=dict(
            family="Arial",
            size=15,
            color='#7F0D04'
        )),
   gauge = {
       'axis': {'range': [None, toptweetertcounts[1]], 'visible': False}, 'bar': {'color': "orange"}},
   domain = {'row': 1, 'column': 2}))




figtoptweeters.update_layout(height=300,
    grid = {'rows': 2, 'columns': 3, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'mode' : "number+gauge",
        'delta' : {'reference': 90}}]
                         }}, margin=dict(r=5, l=5, t=2, b=0))
                         
                         
                         
                         
#TopAssemblies
topassemblylist = df_assembly2['place'].tolist()
topassemblylistcount = df_assembly2['tweetcount'].tolist()


figtopassemblies = go.Figure()

figtopassemblies.add_trace(go.Indicator(
    value = topassemblylistcount[0], title = dict(
        text=topassemblylist[0],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
    gauge = {
        'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
    domain = {'row': 0, 'column': 0}))
figtopassemblies.add_trace(go.Indicator(
    value = topassemblylistcount[1], title = dict(
        text=topassemblylist[1],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
    gauge = {
        'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
    domain = {'row': 0, 'column': 1}))
    
figtopassemblies.add_trace(go.Indicator(
   value = topassemblylistcount[2], title = dict(
        text=topassemblylist[2],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
   gauge = {
       'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
   domain = {'row': 0, 'column': 2}))
   
figtopassemblies.add_trace(go.Indicator(
   value = topassemblylistcount[3], title = dict(
        text=topassemblylist[3],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
   gauge = {
      'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
   domain = {'row': 1, 'column': 0}))
   
figtopassemblies.add_trace(go.Indicator(
   value = topassemblylistcount[4], title = dict(
        text=topassemblylist[4],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
   gauge = {
       'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
   domain = {'row': 1, 'column': 1}))
   
figtopassemblies.add_trace(go.Indicator(
   value = topassemblylistcount[5], title = dict(
        text=topassemblylist[5],
        font=dict(
            family="Arial",
            size=12,
            color='#000000'
        )),
   gauge = {
       'axis': {'range': [None, topassemblylistcount[1]], 'visible': False}, 'bar': {'color': "green"}},
   domain = {'row': 1, 'column': 2}))




figtopassemblies.update_layout(height=300,
    grid = {'rows': 2, 'columns': 3, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'mode' : "number+gauge",
        'delta' : {'reference': 90}}]
                         }}, margin=dict(r=5, l=5, t=2, b=0))
                         
                         




#Metrics part





#fig_metrics = go.Figure(data=[go.Table(
#    header=dict(values=['<b>Total Accounts</b>', '<b>Potential_reach</b>', '<b>Total Tweets</b>' ],
#    fill_color='maroon',
#    align=['center'],
#    font=dict(color='white', size=16),
#    height=40),
#    cells=dict(values=[Count_accounts, TotalReach_humanreadable, int(TotalTweets)],
#                fill_color='white',
#    align=['center'],
#    font=dict(color='black', size=16),
#    height=40))
#])
#fig_metrics.update_layout(title_text='Quick Insights', title_x=0.5)
#
#fig_metrics.update_layout(height=200, margin=dict(r=5, l=5, t=20, b=0))
#
#st.plotly_chart(fig_metrics, use_container_width=True)






fig_metrics = go.Figure()


fig_metrics.add_trace(go.Indicator(
    mode = "number",
    value = Count_accounts, title = dict(
        text='<b>Total Accounts</b>',
        font=dict(
            family="Arial",
            size=15,
            color='#000000'
        )),
    
    domain = {'row': 1, 'column': 0}))
    
fig_metrics.add_trace(go.Indicator(
    mode = "number",
    value = TotalReach, title = dict(
        text='<b>Potential Reach</b> for keyword <b>"Janasena"</b>',
        font=dict(
            family="Arial",
            size=15,
            color='#000000'
        )),
    
    domain = {'row': 0, 'column': 1}))    
    
    
fig_metrics.add_trace(go.Indicator(
    mode = "number",
    value = int(count), title = dict(
        text='<b>Total Tweets</b>',
        font=dict(
            family="Arial",
            size=15,
            color='#000000'
        )),
    
    domain = {'row': 1, 'column': 2}))  



fig_metrics.update_layout(
    grid = {'rows': 3, 'columns': 3, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'mode' : "number+gauge",
        'delta' : {'reference': 120}}]
                         }}, paper_bgcolor = "white", font = {'color': "darkred", 'family': "Arial"})




fig_metrics.update_layout(showlegend=False, autosize=False,
        width=300, height=300, margin=dict(r=0, l=10, t=20, b=0))












 
   
col1, col2, col3= st.columns([1, 2, 1], gap="Large")


with col1:
    st.plotly_chart(fig_metrics, use_container_width=True)
    
    
with col2:

    original_title = '<p style="text-align: center; color:red; font-size: 20px;"><b>Quick Insights</b></p>'
    st.markdown(original_title, unsafe_allow_html=True)
    #st.markdown('##') 
    st.plotly_chart(fig9, use_container_width=True)



with col3:
    mapselect = st.selectbox('Select graph type',[ "Tweet Density Map", "Bar graph", "Scatter Map", "Bubble Map"])
    
    if(mapselect == "Tweet Density Map"):
        st.write('<style>div.block-container{padding-bottom:8rem;}</style>', unsafe_allow_html=True)
        fig_city1.update_layout(autosize=False, margin=dict(r=5, l=5, t=2, b=10), height=200)
        st.plotly_chart(fig_city1, use_container_width=True)
    
    elif(mapselect == "Bar graph"):
        st.write('<style>div.block-container{padding-bottom:8rem;}</style>', unsafe_allow_html=True)
        fig_city4.update_layout(autosize=False, margin=dict(r=5, l=5, t=2, b=10), height=200)
        st.plotly_chart(fig_city4, use_container_width=True)
    elif(mapselect == "Scatter Map"):
        st.write('<style>div.block-container{padding-bottom:8rem;}</style>', unsafe_allow_html=True)
        fig_city2.update_layout(autosize=False, margin=dict(r=5, l=5, t=2, b=10), height=200)
        st.plotly_chart(fig_city2, use_container_width=True)
    elif(mapselect == "Bubble Map"):
        st.write('<style>div.block-container{padding-bottom:8rem;}</style>', unsafe_allow_html=True)
        fig_city3.update_layout(autosize=False, margin=dict(r=5, l=5, t=2, b=10), height=200)
        st.plotly_chart(fig_city3, use_container_width=True)
        
        
        
        
        
        


#st.markdown('#') 


col4, col5, col6= st.columns([1, 1 , 1])


with col4:
    original_title = '<font color=#000000><b>TOP 10 Users By Tweet Counts</b></font> <font color=red>  RED=JSP</font><font color=blue>  BLUE=YCP</font>'
    #original_title = '<p style="text-align: center; color:#970404; font-size: 20px;">TOP 10 Users By Tweet Counts (Blue text --> YCP accounts) </p>'
    #(RED - JSP    BLUE - YCP)
    st.markdown(original_title, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: #970404;'>TOP 10 By Tweet Counts</h1>", unsafe_allow_html=True) 
    #st.markdown("<h1 style='text-align: center; color: red;'>Top 10 Tweeters</h1>", unsafe_allow_html=True)
    #fig16.update_layout(title_text='Top 10 Tweeters', title_x=0.5, height=250, margin=dict(r=5, l=5, t=30, b=10))
    st.plotly_chart(figtoptweeters, use_container_width=True)

        
with col5:

    
    toptweetselect = st.selectbox('Please choose an option',["Top Tweets By Retweets", "Top Tweets By Likes"])
    if(toptweetselect == "Top Tweets By Retweets"):
    
        fig10 = go.Figure(data=[go.Table(   columnorder = [1,2, 3], columnwidth = [40,80,20],
            header=dict(values=list(popularbyretweets_df_new.columns),
                        fill_color='red',
                        font=dict(color='white', family="Lato", size=10),
                        align='center'),
            cells=dict(values=[popularbyretweets_df_new.Username.head(10),  popularbyretweets_df_new.Tweet.head(10), popularbyretweets_df_new.retweets.head(10)],
                    fill_color='white',
                    align='center'))
        ])
        #fig10.update_layout(title_text='Top Tweets By Retweets', title_x=0.5)
        fig10.update_layout(autosize=False, margin=dict(r=5, l=5, t=2, b=0), height=250)
        
        st.plotly_chart(fig10, use_container_width=True)
        
            
#########################################

    
    if(toptweetselect == "Top Tweets By Likes"):    
        fig11 = go.Figure(data=[go.Table(
            header=dict(values=list(popularbylikes_df_new.columns),
                        fill_color='red',
                        font=dict(color='white', family="Lato", size=15),
                        align='center'),
            cells=dict(values=[popularbylikes_df_new.Username.head(10),  popularbylikes_df_new.Tweet.head(10), popularbylikes_df_new.Likes.head(10)],
                    fill_color='white',
                    align='center'))
        ])
        #fig11.update_layout(title_text='Top Tweets By Likes', title_x=0.5)
        fig11.update_layout(autosize=False, margin=dict(r=0, l=0, t=2, b=10), height=250)
        
        st.plotly_chart(fig11, use_container_width=True)
#########################################



with col6:
    original_title = '<font color=#000000><b>TOP 10 Constituencies</b></font>' 
    st.markdown(original_title, unsafe_allow_html=True)
    #st.markdown("<h1 style='text-align: center; color: red;'>Top 10 Assemblies</h1>", unsafe_allow_html=True)
    #fig15.update_layout(title_text='Top 10 Assemblies', title_x=0.5, height=250, margin=dict(r=5, l=5, t=30, b=10))
    st.plotly_chart(figtopassemblies, use_container_width=True)

st.markdown('##')
st.markdown('Jai Janasena ✊')


