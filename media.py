"""defines media types"""


class Movie(object):
    """a light container for movie as it pertains
    to the entertainment center module's usage"""
    def __init__(self, movie_title, movie_trailer, poster_url):
        self.title = movie_title
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster_url
