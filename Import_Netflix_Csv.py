import sqlalchemy as sql
import csv
import pandas as pd

# df = pd.read_csv('netflix_titles.csv')
# print(df)


# quick setup mysql
mydb = sql.create_engine('mysql+pymysql://netflix-demo:root@34.122.76.158/netflixdemo')

conn = mydb.connect()

with open('netflix_titles.csv', 'r', encoding='utf-8') as csvFile:
    csv_reader = csv.reader(csvFile)

    next(csv_reader)

    type_list = []
    title_list = []
    director_list = []
    cast_list = []
    country_list = []
    rating_list = []
    listed_in_list = []
    movie_list = []
    movie_cast_list = []
    movie_director_list = []
    movie_country_list = []
    movie_rating_list = []
    movie_current_listed = []

    for i, item in enumerate(csv_reader, start=1):
        # process csv into unique tables

        # add type to type list
        movie_type_list = []
        if item[1] not in type_list:
            type_list.append(item[1])

        movie_type_list.append(str(type_list.index(item[1])))

        # convert directors to their own list and process that
        current_directors = item[3].split(",")

        for director in current_directors:
            director = director.strip()
            if director not in director_list:
                director_list.append(director)

            director_to_movie = {'content_id': i, 'director_id': director_list.index(director)+1}
            movie_director_list.append(director_to_movie)

        # convert cast to their own list and process that
        current_cast = item[4].split(",")

        for cast in current_cast:
            cast = cast.strip()
            if cast not in cast_list:
                # this is to create the actors table later
                cast_list.append(cast)

            cast_to_movie = {'content_id': i, 'actor_id': cast_list.index(cast)+1}
            movie_cast_list.append(cast_to_movie)

        # convert country to their own list and process that
        current_country = item[5].split(",")
        for country in current_country:
            country = country.strip()
            if country not in country_list:
                country_list.append(country)

            country_to_movie = {'content_id': i, 'country_id': country_list.index(country)+1}
            movie_country_list.append(country_to_movie)

        # convert rating to their own list and process that
        current_rating = item[8].split(",")
        for rating in current_rating:
            rating = rating.strip()

            if rating not in rating_list:
                rating_list.append(rating)

            rating_to_movie = {'content_id': i, 'rating_id': rating_list.index(rating)+1}
            movie_rating_list.append(rating_to_movie)

        # convert listed in to their own list and process that
        current_listed = item[10].split(",")
        for listed in current_listed:
            listed = listed.strip()
            if listed not in listed_in_list:
                listed_in_list.append(listed)

            movie_current = {'content_id': i, 'movie_category': listed_in_list.index(listed)+1}
            movie_current_listed.append(movie_current)

        # now create a movie record and add it to the movie list
        movie_dict = dict()
        movie_dict['type'] = item[1]
        movie_dict['title'] = item[2]
        movie_dict['date_added'] = item[6]
        movie_dict['release_year'] = item[7]
        movie_dict['rating'] = item[8]
        movie_dict['duration'] = item[9]
        movie_dict['description'] = item[11]

        movie_list.append(movie_dict)

actordf = pd.DataFrame(cast_list, columns=['name'])
actordf.to_sql('actors', mydb, if_exists='append', index=False)

countrydf = pd.DataFrame(country_list, columns=['name'])
countrydf.to_sql('countries', mydb, if_exists='append', index=False)

directordf = pd.DataFrame(listed_in_list, columns=['name'])
directordf.to_sql('categories', mydb, if_exists='append', index=False)

directordf = pd.DataFrame(director_list, columns=['name'])
directordf.to_sql('director', mydb, if_exists='append', index=False)

rating_listdf = pd.DataFrame(rating_list, columns=['name'])
rating_listdf.to_sql('rating', mydb, if_exists='append', index=False)

moviedf = pd.DataFrame(movie_list)
moviedf.to_sql('content', mydb, if_exists='append', index=False)

actor_to_movie_df = pd.DataFrame(movie_cast_list)
actor_to_movie_df.to_sql('actors_to_movie', mydb, if_exists='append', index=False)

director_to_movie_df = pd.DataFrame(movie_director_list)
director_to_movie_df.to_sql('director_to_movie', mydb, if_exists='append', index=False)

country_to_movie_df = pd.DataFrame(movie_country_list)
country_to_movie_df.to_sql('country_to_movie', mydb, if_exists='append', index=False)

movie_rating_to_movie_df = pd.DataFrame(movie_rating_list)
movie_rating_to_movie_df.to_sql('movie_rating_to_movie', mydb, if_exists='append', index=False)

movie_current_to_movie_df = pd.DataFrame(movie_current_listed)
movie_current_to_movie_df.to_sql('movie_category_to_movie', mydb, if_exists='append', index=False)

print('end')
