import webbrowser

class Movie():
    """ This class provides a way to store data related to movie """  
    def __init__(self,title,storyline,poster_image,youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
