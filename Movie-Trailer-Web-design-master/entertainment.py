import media
import fresh_tomatoes

# Zootopia
zootopia = media.Movie("Zootopia ",
                       """Zootopia is a 2016 American 3D computer-animated 
                        comedy-adventure film produced by Walt Disney Animation Studios
                        and released by Walt Disney Pictures.""",
                        "http://www.moviemagik.in/files/posters/3558/zootopia.jpg",
                        "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# The Jungle Book
jungle_book = media.Movie("The Jungle Book ",
                        "The Jungle Book is a 2016 American fantasy adventure musical film",
                        "http://www.impawards.com/2016/posters/jungle_book_ver6_xlg.jpg",
                        "https://www.youtube.com/watch?v=5mkm22yO-bs")

# Deadpool
deadpool = media.Movie("Deadpool ",
                        """Deadpool is a 2016 American superhero film directed by Tim Miller and 
                        written by Rhett Reese and Paul Wernick, based on the Marvel Comics 
                        character of the same name. """,
                        "http://www.joblo.com/posters/images/full/Deadpool-poster-6.jpg",
                        "https://www.youtube.com/watch?v=ZIM1HydF9UA")

# The Martian
martian = media.Movie("The Martian ",
                       """The Martianis a 2015 American science fiction novel written
                       by Andy Weir. It was his debut novel under his own name. """,
                       "http://www.impawards.com/2015/posters/martian_ver6_xxlg.jpg",
                       "https://www.youtube.com/watch?v=ej3ioOneTy8")

# Everest
everest = media.Movie("Everest ",
                      """Everest is a 2015 mountain adventure file directed by Baltasar
                       Kormakur and written by William Nicholoson and Simon Beaufoy. """,
                      "http://www.impawards.com/2015/posters/everest.jpg",
                      "https://www.youtube.com/watch?v=79Q2rrQlPW4")

# Interstellar
interstellar  = media.Movie("Interstellar ",
                            "A story of space travel",
                            "https://d3ui957tjb5bqd.cloudfront.net/uploads/2014/11/interstellar-poster-18.jpg",
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [zootopia,jungle_book,deadpool,martian,everest,interstellar]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
