# movie-app
 final project

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jinghualuo-movie-app-movie-industry-vsl00y.streamlitapp.com/) 


Hi, there! This app visualizes the data of movie industry between 1980-2020 and builds interactive function with [Streamlit](https://streamlit.io/). It gives us the overview of movie industry, play fun with it!

![image](https://github.com/JinghuaLuo/movie-app/blob/main/app-screenshot.png)

## Table of Contents

- [Install](#install)
- [Usage](#usage)


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

pandas
```
movie = pd.read_csv('movies.csv')
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

plotly
```
percentage_of_share = (movie.genre.value_counts()/len(movie.genre))*100
fig_pie = px.pie(values=percentage_of_share, names=movie.genre.unique(), title='The share of Genre Types', opacity=0.7)
fig_pie.update_traces(textposition='inside')
fig_pie.update_layout(uniformtext_minsize=4, uniformtext_mode='hide')
```

