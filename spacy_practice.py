import spacy
import time

start_time = time.time()
nlp = spacy.load("en_core_web_md")
tokens = nlp("cat apple monkey banana")
print("Initialization took --- %s seconds ---" % round((time.time() - start_time), 6))

start_time = time.time()
for token_a in tokens:
    for token_b in tokens:
        print(token_a.text, token_b.text, token_a.similarity(token_b))
print("Nested for took --- %s seconds ---" % round((time.time() - start_time), 6))