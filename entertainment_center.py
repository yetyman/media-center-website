import media

#instantiating the movie class
m = media.Movie("its joke","https://www.youtube.com/watch?v=D8cvgQJFDeo","https://memes3.fjcdn.com/comments/Blank+_e3f147720c601dd7cb9e02fa45ca27b3.jpg")
j = media.Movie("oh hi mark","https://www.youtube.com/watch?v=Z9cB0TjfIkM","https://docs.python.org/2.7/_static/py.png")
k = media.Movie("do u kno da wei?","https://www.youtube.com/watch?v=H34qrTkhFz0","https://i.guim.co.uk/img/media/794bb19154c0c0c3cfa2bc0b3f0e805f15cc2329/721_243_4595_2757/master/4595.jpg?w=1750&q=55&auto=format&usm=12&fit=max&s=654ed36d3271578f6317efa6786b93a4")
movs = [m,j,k]

#generating and opening the web page
fresh_tomatoes.open_movies_page(movs)