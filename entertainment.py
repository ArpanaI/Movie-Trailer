import media
import fresh_tomatoes

# Create instances of the Movie class to hold information of my favourite
# movies.
# Each Instance holds the following information
# Movie Title, Movie Storyline, Poster Image, Youtube Trailer,
# Year and month of Release

interstellar = media.Movie(
                            "Interstellar",
                            "A team of explorers travel through a wormhole in\
                            space in an attempt to ensure humanity's survival",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/"
                            "Interstellar_film_poster.jpg",
                            "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                            "March,2015")

inception = media.Movie(
                        "Inception",
                        "A professional thief who steals information by\
                        infiltrating the subconscious",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                        "Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "Jan,2010")

avatar = media.Movie(
                        "Avatar",
                        "A story on Aliens",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                        "Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8&t=2s",
                        "April,2009")


school_of_rock = media.Movie(
                            "School Of Rock",
                            "Playing rock to teach students",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/"
                            "School_of_Rock_Poster.jpg",
                            "https://www.youtube.com/watch?v=5afGGGsxvEA",
                            "June,2003")

troy = media.Movie(
                    "Troy",
                    "A prince falls for a king's wife and takes her along\
                    with him to Troy. The king's brother then uses this as an\
                    excuse to rage war on Troy and realise his own selfish\
                    motives.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/"
                    "Troy2004Poster.jpg",
                    "https://www.youtube.com/watch?v=QpikTTSOHXc", "Feb,2004")

toyStory = media.Movie(
                        "Toy Story",
                        "In a world where anthropomorphic toys pretend to be\
                        lifeless whenever humans are present",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=1guCjulfnZI",
                        "Nov,1995")

everest = media.Movie(
                        "Everest",
                        "Two groups, one led by Rob Hall and the other by\
                        Scott Fischer, encounter several challenges and\
                        threatening weather conditions as they attempt to\
                        scale Mount Everest.",
                        "https://upload.wikimedia.org/wikipedia/en/2/28/"
                        "Everest_poster.jpg",
                        "https://www.youtube.com/watch?v=79Q2rrQlPW4",
                        "Sept 2015")

castAway = media.Movie(
                        "Cast Away",
                        "Chuck Noland wakes up on a deserted island after his\
                        plane crash-lands in the Pacific. He must harness\
                        every skill he knows to survive the mental and\
                        physical agony of living alone.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a7/"
                        "Cast_away_film_poster.jpg",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs",
                        "Dec 2015")

titanic = media.Movie(
                        "Titanic",
                        "A fictionalized account of the sinking of the RMS\
                        Titanic, it stars Leonardo DiCaprio and Kate Winslet\
                        as members of different social classes who fall in\
                        love aboard the ship during its ill-fated maiden\
                        voyage.",
                        "https://upload.wikimedia.org/wikipedia/en/2/22/"
                        "Titanic_poster.jpg",
                        "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
                        "Aug 1997")

# Add the instances to a list
movies = [
            interstellar, inception, troy, school_of_rock, avatar, toyStory,
            everest, castAway, titanic]

# Generate a web page that displays the movies in the list

fresh_tomatoes.open_movies_page(movies)
