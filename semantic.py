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
    """ """
    start = time.time()
    for token_a in tokens:
        for token_b in tokens:
            print(token_a.text, token_b.text, end=" ")
            if token_a.similarity(token_b) > 0.5:
                print(GREEN + BOLD + f"{token_a.similarity(token_b)}" + ESCAPE)
            else:
                print(token_a.similarity(token_b))

    print(CYAN + BOLD + message + f" took --- {round((time.time() - start), 6)} seconds ---" + ESCAPE)


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



