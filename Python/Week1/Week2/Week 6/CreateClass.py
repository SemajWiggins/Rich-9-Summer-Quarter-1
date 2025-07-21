# 1. Create a class to represent a Video Game or Movie Collection
# 2. Create a constructor method __init__()
# 3. Create a list for the video games and movies each
# 4. Create a instance variable for the user's favorite movie and video game respectively
# 5. Create the following functions for your class
# - A function to display all the movies
# - A function to display all the video game
# - A function to add a movie/video game
# - A function to remove a move/video game
# - A function to select a favorite video game and or movie
# 6. Crate a seperate tester.py file to test your code

class Collection:
    def __init__(self, movieList, gameList):
        self.movieList = movieList
        self.gameList = gameList
        self.favGame = ""
        self.favMovie = ""

    def add_game(self, game):
        if game in self.gameList:
            print("Game is already in collection")
        else:
            self.gameList.append(game)

    def add_movie(self, movie):
        if movie in self.movieList:
            print("Movie is already in collection")
        else:
            self.movieList.append(movie)

    def remove_game(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("Game Not Found")

    def remove_movie(self, movie):
        if movie in self.movieList:
            self.movieList.remove(movie)
        else:
            print("Movie Not Found")

    def display_movies(self):
        print("Movies in your collection:")
        for movie in self.movieList:
            print(f"- {movie}")

    def display_games(self):
        print("Video Games in your collection:")
        for game in self.gameList:
            print(f"- {game}")

    def display_fav_game(self):
        print(f"Favorite Game: {self.favGame}")

    def display_fav_movie(self):
        print(f"Favorite Movie: {self.favMovie}")

    def display_collection(self):
        self.display_movies()
        self.display_fav_movie()
        self.display_games()
        self.display_fav_game()

    def set_fav_movie(self, movie):
        if movie not in self.movieList:
            self.add_movie(movie)
        self.favMovie = movie

    def set_fav_game(self, game):
        if game not in self.gameList:
            self.add_game(game)
        self.favGame = game
