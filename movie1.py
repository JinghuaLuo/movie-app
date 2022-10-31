import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objs as go
import time
plt.style.use('seaborn')

# read the csv file
movie = pd.read_csv('movies.csv')

# deal with the NAN data
# drop budget column and some rows
movie.drop(['budget'], axis=1, inplace=True)
movie.dropna(subset = ['rating', 'score', 'votes', 'writer', 'star', 'country', 'company', 'runtime'], inplace=True)
# fill with rating and gross
# rating is categorical
most_freq = movie.rating.value_counts().idxmax()
movie.rating.fillna(most_freq, inplace=True)
# gross is numerical
movie.gross.fillna(movie.gross.mean(), inplace=True)

# picture
col1, col2, col3, col4, col5 = st.columns(5, gap="small")
with col1:
   st.image("picture6.jpg", width=150)

with col2:
   st.image("picture5.jpg", width=150)

with col3:
   st.image("picture41.png", width=150)

with col4:
   st.image("picture9.jpg", width=150)

with col5:
   st.image("picture8.jpg", width=150)


# title
st.title('Movie Industry')

#line chart：Growth Rate
gross_for_year = movie.groupby('year')['gross'].sum()
growth_rate = gross_for_year.pct_change(1).fillna(0)
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=movie.year.unique(), y=growth_rate, mode='lines+markers'))
fig_line.update_traces(marker_color='#FF4B4B')
fig_line.update_layout(title='Growth Rate of Gross', xaxis_title='Year', yaxis_title='Growth Rate', yaxis=dict(tickformat='.1%'))

# Top10 countries with the largest amount of movies
top_country = movie.country.value_counts(ascending=True)[-10:]
fig_bar = px.bar(
    top_country,
    orientation='h',
    title='Top10 countries with the largest amount of movies',
    opacity=0.7
    )
fig_bar.update_layout(xaxis_title='Number of Movies', yaxis_title='Country')
fig_bar.update_traces(marker_color='#FF4B4B')

# pie plot: Genre
percentage_of_share = (movie.genre.value_counts()/len(movie.genre))*100
fig_pie = px.pie(values=percentage_of_share, names=movie.genre.unique(), title='The share of Genre Types', opacity=0.7)
fig_pie.update_traces(textposition='inside')
fig_pie.update_layout(uniformtext_minsize=4, uniformtext_mode='hide')

# wordcloud: director
fig_pwordcloud, ax = plt.subplots(figsize=(11, 7))
worldcloud = WordCloud(
    background_color = 'Black',
    width = 1920,
    height = 1080
).generate(" ".join(movie.director))
plt.imshow(worldcloud)
plt.axis('off')

# tab: 合并前四张
tab1, tab2, tab3, tab4 = st.tabs(['Growth Rate', 'Top10 countries', 'Genre Pie', 'Director Wordcloud'])
with tab1:
    st.plotly_chart(fig_line)
with tab2:
    st.plotly_chart(fig_bar)
with tab3:
    st.plotly_chart(fig_pie)
with tab4:
    st.markdown('###### The worldcloud of directors')
    st.pyplot(fig_pwordcloud)

#slider: score
score_slider = st.sidebar.slider('Score of the movie', 1.0, 10.0, 7.0)
movie = movie[movie.score >= score_slider]

#sidebar: multiselect at most 2 countries
country_filter= st.sidebar.multiselect(
    'Choose at most 2 countries',
    movie.country.unique()
)
movie = movie[movie.country.isin(country_filter)]

#sidebar: choose year
year_filter = st.sidebar.radio(
    'Choose the year of the movie you want: ',
    ('1980-1990', '1990-2000', '2000-2010', '2010-2020', 'All')
)
if year_filter == '1980-1990':
    movie = movie[(movie.year >= 1980) & (movie.year <= 1990)]
if year_filter == '1990-2000':
    movie = movie[(movie.year > 1990) & (movie.year <= 2000)]
if year_filter == '2000-2010':
    movie = movie[(movie.year > 2000) & (movie.year <= 2010)]
if year_filter == '2010-2020':
    movie = movie[(movie.year > 2010) & (movie.year <= 2020)]
if year_filter == 'All':
    movie = movie

#barplot: number of movies in a country
if movie.empty:
    st.warning('Empty! Please choose at least two countries in the sidebar', icon="⚠️")
else:
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    movies_of_country = movie.groupby('country').year.value_counts().sort_index(ascending=True)

    movies_of_country = movies_of_country.to_frame()
    movies_of_country = movies_of_country.rename(columns={'year': 'value'})
    movies_of_country = movies_of_country.reset_index()

    fig_bar2 = px.bar(movies_of_country, x='year', y='value', color='country', barmode='group', opacity=0.7)
    fig_bar2.update_layout(
        title='The Number of Movies in the Country',
        xaxis_title='Year',
        yaxis_title='Number of Movies',
        )
    st.plotly_chart(fig_bar2)

#show the dataframe
st.write(movie)

