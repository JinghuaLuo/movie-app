# movie-app
 final project

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jinghualuo-movie-app-movie-industry-vsl00y.streamlitapp.com/) 


Hi, there! This app visualizes the data of movie industry between 1980-2020 and builds interactive function with [Streamlit](https://streamlit.io/). It gives us the overview of movie industry, play fun with it!

![image](https://github.com/JinghuaLuo/movie-app/blob/main/app-screenshot.png)

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Coding Style](#codingstyle)

## Install

```
pip install pandas
pip install matplotlib
pip install streamlit
pip install wordcloud
pip install plotly
pip install time
```

Streamlit can also be installed in a virtual environment on Windows, Mac, and Linux.

## Usage

deal with missing data using drop,dropna, fillna
```
movie.drop(['budget'], axis=1, inplace=True)
movie.dropna(subset = ['rating', 'score', 'votes', 'writer', 'star', 'country', 'company', 'runtime'], inplace=True)
most_freq = movie.rating.value_counts().idxmax()
movie.rating.fillna(most_freq, inplace=True)
movie.gross.fillna(movie.gross.mean(), inplace=True)
```

wordcloud
```
fig_pwordcloud, ax = plt.subplots(figsize=(11, 7))
worldcloud = WordCloud(
    background_color = 'Black',
    width = 1920,
    height = 1080
).generate(" ".join(movie.director))
plt.imshow(worldcloud)
plt.axis('off')
```

pie chart
```
percentage_of_share = (movie.genre.value_counts()/len(movie.genre))*100
fig_pie = px.pie(values=percentage_of_share, names=movie.genre.unique(), title='The share of Genre Types', opacity=0.7)
fig_pie.update_traces(textposition='inside')
fig_pie.update_layout(uniformtext_minsize=4, uniformtext_mode='hide')
```

line chart
```
gross_for_year = movie.groupby('year')['gross'].sum()
growth_rate = gross_for_year.pct_change(1).fillna(0)
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=movie.year.unique(), y=growth_rate, mode='lines+markers'))
fig_line.update_traces(marker_color='#FF4B4B')
fig_line.update_layout(title='Growth Rate of Gross', xaxis_title='Year', yaxis_title='Growth Rate', yaxis=dict(tickformat='.1%'))
```
grouped bar chart
```
fig_bar2 = px.bar(movies_of_country, x='year', y='value', color='country', barmode='group', opacity=0.7)
fig_bar2.update_layout(
    title='The Number of Movies in the Country',
    xaxis_title='Year',
    yaxis_title='Number of Movies',
    )
```


## Coding Style
The coding style is UTF-8



