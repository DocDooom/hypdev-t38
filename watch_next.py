# Overview: HyperionDev Task 38 Semantic Similarity
# Given a movie description, suggest the most similar movie to watch next

# Import NLP library SpaCy
import spacy

# Load English Language pack
nlp = spacy.load("en_core_web_md")


# We're defining a function here to process our description string
# Against a dictionary of movies and their descriptions
# from this we'll return the key of the dictionary item with the highest similarity
def recommend_move(description: str, mov_dict: dict) -> str:
    """ This function returns the key of the dictionary item with the highest similar to
    comparison description

    Arguments

    description - is a string which we will compare our dictionary to
    mov_dict - is a dictionary of description which we'll try to find the closest
    description to our description param

    Returns a key indicating the highest match"""
    description = nlp(description)
    similarity_dict = {}

    for description in mov_dict:
        similarity = nlp(description).similarity(description)
        similarity_dict[description] = similarity

    return max(similarity_dict, key=lambda x: similarity_dict[x])


# Initialize dictionary to use with our function
movies_dict = {}

# Open our movies.txt file and create a dictionary from it
with open("movies.txt", "r", encoding="utf-8") as movies_file:
    for line in movies_file:
        movie, movie_description = line.split(":")

        movies_dict[movie] = movie_description

# Our comparison description
initial_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous" \
                      "for the Earth, the illuminati trick the Hulk into a shuttle and launch him" \
                      "into space to a planet where the Hulk can live in peace. Unfortunately, Hulk" \
                      "lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"

# OUTPUT
print("The recommended movie to watch next is: ")
print(recommend_move(initial_description, movies_dict),
      movies_dict[recommend_move(initial_description, movies_dict)])
