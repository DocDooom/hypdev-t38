import spacy
from spacy.tokens import Doc

movies_dict = {}


def recommend_move(movie_desc: str, movies_dict: dict):
    for description in movies_dict:
        similarity = nlp(description).similarity(model_sentence)
        print(sentence + " - ", similarity)


with open("movies.txt", "r", encoding="utf-8") as movies_file:
    for line in movies_file:
        movie, movie_description = line.split(":")

        movies_dict[movie] = movie_description

