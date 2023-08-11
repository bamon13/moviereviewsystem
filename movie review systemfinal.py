class MovieReviewSystem:
    def __init__(self):
        self.movies = {}
    
    def add_movie(self, title, genre):
        self.movies[title] = {'genre': genre, 'ratings': [], 'reviews': []}
    
    def rate_movie(self, title, rating):
        if title in self.movies:
            self.movies[title]['ratings'].append(rating)
            print(f"Rated {title} with {rating} stars.")
        else:
            print(f"{title} not found in the movie list.")
    
    def review_movie(self, title, review_text):
        if title in self.movies:
            self.movies[title]['reviews'].append(review_text)
            print(f"Reviewed {title}: {review_text}")
        else:
            print(f"{title} not found in the movie list.")
    
    def get_average_rating(self, title):
        if title in self.movies:
            ratings = self.movies[title]['ratings']
            if ratings:
                return sum(ratings) / len(ratings)
            else:
                return 0
        else:
            return None
    
    def list_movies(self):
        for title in self.movies:
            print(title)
    
    def get_movie_details(self, title):
        if title in self.movies:
            details = self.movies[title]
            genre = details['genere']
            avg_rating = self.get_average_rating(title)
            reviews = details['reviews']
            
            print(f"Title: {title}")
            print(f"Genre: {genre}")
            if avg_rating is not None:
                print(f"Average Rating: {avg_rating:.2f}")
            else:
                print("Average Rating: N/A")
            
            print("Reviews:")
            for review in reviews:
                print(review)
        else:
            print(f"{title} not found in the movie list.")
    
# Create an instance of the MovieReviewSystem
review_system = MovieReviewSystem()

# Adding movies
review_system.add_movie("Jailer", "Crime Thriller")
review_system.add_movie("Varisu", "sentiment")
review_system.add_movie("Thunivu", "Heist Thriller")
review_system.add_movie("Vikram", "Action-thriller")

# Rating and reviewing movies
review_system.rate_movie("Jailer", 4.0)
review_system.rate_movie("Varisu", 4.0)
review_system.rate_movie("Thunivu", 3.5)
review_system.rate_movie("Vikram", 4.5)

review_system.review_movie("Jailer", "தலைவர் நிரந்தரம்!")
review_system.review_movie("Varisu", "குடும்பங்கள் கொண்டாடும் வெற்றி.")
review_system.review_movie("Thunivu", "The ReaL Winner.")
review_system.review_movie("Vikram", "Ghost Returns!.")

# Displaying movie details
review_system.get_movie_details("Jailer")
review_system.get_movie_details("Varisu")
review_system.get_movie_details("Thunivu")
review_system.get_movie_details("Vikram")

# Listing all movies
print("All movies:")
review_system.list_movies()
