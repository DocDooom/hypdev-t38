import spacy
from spacy.tokens import Doc
import time

# Styling
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
ESCAPE = "\033[00m"
CYAN = "\033[96m"
PURPLE = "\033[35m"
BOLD = "\033[1m"


def compare(tokens: Doc, message: str) -> None:
    """ This function takes in a spaCy doc token and compares each of those tokens
    with one another, the function also outputs the time taken

    Arguments

    tokens - of type spaCy Doc - a tokenized string of words
    message - a string containing the output message you'd like to include when outputting the time taken"""
    start = time.time()

    for token_a in tokens:
        for token_b in tokens:
            print(token_a.text, token_b.text, end=" ")
            if token_a.similarity(token_b) > 0.5:
                print(GREEN + BOLD + f"{token_a.similarity(token_b)}" + ESCAPE)
            else:
                print(token_a.similarity(token_b))

    print(CYAN + BOLD + message + f" took --- {round((time.time() - start), 6)} seconds ---" + ESCAPE)


# ---- PART 1 ----
print("---- PART 1 ---")

# load language model
start_time = time.time()
nlp = spacy.load("en_core_web_md")
print(CYAN + BOLD + f"Loading complex language model "
                    f"took --- {round((time.time() - start_time), 6)} seconds ---" + ESCAPE)

token_1 = nlp("cat apple monkey banana")
token_2 = nlp("book paper library worm")

# It is interesting that cat and monkey are less similar than apple and banana
compare(token_1, "Token 1")
# I'm surprised by the low similarity book and worm - however this makes sense as spaCy seems to be comparing
# words and not taking into account "book worm" is a popular phrase.
compare(token_2, "Token 2")

# ---- PART 2 ----
print("---- PART 2 ---")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Note: "Hello, there is my car" has a similarity of around 0.8 it seems this is because the sentence contains a
# good amount of words that the sentence "Why is my cat on the car" contains

