FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
"title": "The JavaScript and the React",
"genre": "Action",
"rating": 2.2
}

INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
HORROR_1 = {
    "title": "It Came from the Stack Trace",
    "genre": "Horror",
    "rating": 3.5
}

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None

    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_movie = user_data['watched']
    movie_to_watchlist = user_data['watchlist']

    for item in movie_to_watchlist:
        if title == item['title']:
            watched_movie.append(item)
            movie_to_watchlist.remove(item)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_movies = len(user_data["watched"])

    if len(user_data["watched"]) == 0:
        return 0.0
    
    for i in range(len(user_data["watched"])):
            total_ratings += user_data["watched"][i]["rating"]
            average_rating = total_ratings / number_movies
    return average_rating



def get_most_watched_genre(user_data):
    genre_options = []

    if user_data["watched"] == []:
        return None    
    
    for i in range(len(user_data["watched"])):
        genre_options.append(user_data["watched"][i]["genre"])
        highest_watched = (max(set(genre_options), key=genre_options.count))
    return highest_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    unique_watch = []
    friends_movies_watched = []

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_movies_watched.append(movie)
 
    for movie in user_data["watched"]:
        if movie not in friends_movies_watched:
            unique_watch.append(movie)
    return unique_watch

  
def get_friends_unique_watched(user_data):
    # user_data = {
    # "watched": [
    # FANTASY_1, 
    # FANTASY_2, 
    # FANTASY_3, 
    # ACTION_1, 
    # INTRIGUE_1, 
    # INTRIGUE_2
    # ], "friends": [
    # {
    #     "watched": [
    #         FANTASY_1,
    #         FANTASY_3,
    #         FANTASY_4,
    #         HORROR_1,
    #     ]
    # },
    # {
    #     "watched": [
    #         FANTASY_1,
    #         ACTION_1,
    #         INTRIGUE_1,
    #         INTRIGUE_3,
    #     ]
    # }
    # ]}

    unique_watch = []
    no_duplicate_unique_watch = []
   

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"]:
                    unique_watch.append(movie)

    for movie in unique_watch:
        if movie not in no_duplicate_unique_watch:
            no_duplicate_unique_watch.append(movie)
    return no_duplicate_unique_watch



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_genre = []
    fave_genre = get_most_watched_genre(user_data)
    unique_list_of_movies_watched_by_friends = get_most_watched_genre(user_data)
    user_titles_that_match_my_fave_genre = []

    for movie in user_data["watched"]:
        if movie["genre"] == fave_genre:
            user_titles_that_match_my_fave_genre.append(movie["title"])
    
    for indivd_movie in unique_list_of_movies_watched_by_friends:
        for individ_movie in friend[0]["watched"]:
            if individ_movie["genre"] == fave_genre and movie["title"] not in user_titles_that_match_my_fave_genre:
                recommended_genre.append(individ_movie)
    return recommended_genre





    
    # recommended_genre = []
    # new_list = []
    # fave_genre = get_most_watched_genre(user_data)
   
    # for movie in user_data["friends"]:
    #     for i in movie["watched"]:
    #         new_list.append(i)
    # for movie in new_list:
    #     if movie["genre"] == fave_genre:
    #         recommended_genre.append(movie)
    # return recommended_genre

    
    # for friend in unique_list_of_movies_watched_by_friends:
    #     for indiv_movie in friend["watched"]:
    #         if indiv_movie["genre"] == fave_genre and movie["title"] not in user_title_that_match_my_fave_genre:
    #             recommended_genre.append(indiv_movie)
    # return recommended_genre       
    