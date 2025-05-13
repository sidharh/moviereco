import streamlit as st
import pickle
from operator import itemgetter
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movies_list = movies['title'].values
#movies_list2 = movies['Movie_id'].values

st.header("Movie Recommendation System")

selectvalue = st.selectbox("Select movie from dropdown",movies_list)
#selectvalue = st.selectbox("Select movie id from dropdown",movies_list2)

#def fetch_poster(movie_id):
 #   api_key = "7b58473913f868e6de88752076ff62ed"  # Replace with your TMDb API key
  #  url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
   # response = requests.get(url)
    #if response.status_code == 200:
     #   data = response.json()
      #  poster_path = data.get('poster_path', '')
       # if poster_path:
        #    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
         #   return full_path
    #return None

def fetch_poster(movie_id):
    api_key = "7b58473913f868e6de88752076ff62ed"  # Replace with your TMDb API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
    return None

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), key=itemgetter(1), reverse=True)
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].Movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


if st.button("Show Recommendation"):
    movie_name, movie_poster = recommend(selectvalue)
    if not movie_name:
        st.write("No recommendations found.")
    else:
        cols = st.columns(5)
        for col, name, poster in zip(cols, movie_name, movie_poster):
            with col:
                st.text(name)
                st.image(poster)
