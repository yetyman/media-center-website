import fresh_tomatoes
import webbrowser

class Movie():
    def __init__(itsme,movie_title,movie_trailer, poster_url):
        itsme.title = movie_title
        itsme.trailer_youtube_url = movie_trailer
        itsme.poster_image_url = poster_url
   