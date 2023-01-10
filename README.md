# hypdev-t38 - HyperionDev SE Task 38

# Compulsory Task 1

Interesting Finds from Semantic.py

1. It is interesting that cat and monkey are less similar than apple and banana
2. I compare "book paper library" - I'm surprised by the low similarity of book and worm (and the general low similarity overall)
However this makes sense as spaCy seems to be comparing
words and not taking into account "book worm" is a popular phrase.
3. Finally beyond the obvious warnings given (The model you're using has no word vectors loaded...) it's clear the simpler language model returns overall lower and less varied similarities

# Compulsory Task 2
Please find watch_next.py which covers the requirements for CT 2

We define a function that takes a movie description and dictionary of other movie descriptions, returning the one that is most similar and thus recommended

