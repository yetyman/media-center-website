"""Calls code from fresh_tomatoes to generate and display a static webpage"""
import media
import fresh_tomatoes

def make_movies_list():
    """generate a list of movies from hardcoded values"""
    itsjoke = media.Movie("its joke", "https://www.youtube.com/watch?v=D8cvgQJFDeo", "https://mem"+
                          "es3.fjcdn.com/comments/Blank+_e3f147720c601dd7cb9e02fa45ca27b3.jpg")
    theroom = media.Movie("oh hi mark", "https://www.youtube.com/watch?v=Z9cB0TjfIkM",
                          "https://docs.python.org/2.7/_static/py.png")
    knuckles = media.Movie("do u kno da wei?", "https://www.youtube.com/watch?v=H34qrTkhFz0",
                           ''.join(["https://i.guim.co.uk/img/media/794bb19154c0c0c3cfa2bc0b3f0e8",
                                    "05f15cc2329/721_243_4595_2757/master/4595.jpg?w=1750&q=55&au",
                                    "to=format&usm=12&fit=max&s=654ed36d3271578f6317efa6786b93a4"]))
    return [itsjoke, theroom, knuckles]


#generating and opening the web page
fresh_tomatoes.open_movies_page(make_movies_list())
