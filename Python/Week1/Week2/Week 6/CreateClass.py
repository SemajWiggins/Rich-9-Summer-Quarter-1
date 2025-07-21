# 1. Create a class to represent a Video Game or Movie Collection
# 2. Create a constructor method __init__()
# 3. Create a list for the video games and movies each
# 4. Create a instance variable for the user's favorite movie movie and video game respectively
# 5. Create the following functions for your class
# - A fucntion to display all movies
# - A function to display all the video games
# - A function to add a movie/video game
# - A function to remove a movie/video game
# - A function ot select a favorite movie/video game
# 6. Create a seperate tester.py file to test your code

class Collection:
    def __init__(self, movieList, gameList): # Organizing, taking all the objects in, and creating the list
        self.movieList = []
        self.gameList = []
        self.favgame = ""
        self.favmovie = ""

        self.movieList = movieList
        self.gameList = gameList

        def AddGame(self, game):
            if game in self.gameList:
                print("Game is already in collection")
            else:
                self.gameList.append(game)

        def AddMovie(self, movie):
            if movie in self.movieList:
                print("Movie is already in collection")
            self.movieList.append(movie)

        def RemoveGame(self, game):
            if game not in self.gameList:
                self.gameList.remove(game)
            else:
                print("Game Not Found")
        
        def RemovieMovie(self, movie):
            if movie not in self.gameList:
                self.movieList.remove(movie)
            else:
                print("Movie Not Found")

        def display_Movies(self):
            print("Movies in your collection:")
        for movie in self.movieList:
            print(f"- {movie}")

        def display_Games(self):
            print("Video Games in your collection:")
        for game in self.gameList:
            print(f"-{game}")

        def DisplayFavGame(self):
            print(f'Fav Game{self.favGame}')

        def DisplayFavMovie(self):
            print(f'Fav Game {self.favMovie}')

        def DisplayCollection(self):
            self.DisplayMovies()
            self.DisplayFavMovies()
            self.DisplayGames()
            self.DisplayFavGames()
        
        def SetFavMovie(self, movie):
            if movie not in self.movieList:
                self.AddMovie(movie)
            self.favMovie = movie

        def SetFavGame(self, game):
            if movie not in self.movieList:
                self.AddGame(game)
            self.favGame(game)
