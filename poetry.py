"""
    Generate a poem from lists of words
"""
from random import choice

# Words to generate a poem from
nouns = ["car", "plane", "boat"]
verbs = ["ride", "fly", "swim"]
adjectives = ["fast", "amazing", "wonderful"]
prepositions = ["against", "after", "into", "beneath"]
adverbs = ["curiously", "tantalizingly", "sensuously"]

def makePoem():
    """ Generate a poem """
    # Select random words
    # Select nouns
    n1 = choice(nouns)
    n2 = choice(nouns)
    n3 = choice(nouns)
    # Make sure nouns are unique
    while n1 == n2:
        n1 = choice(nouns)
    while n3 == n1 or n3 == n2:
        n3 = choice(nouns)
    
    # Select verbs
    v1 = choice(verbs)
    v2 = choice(verbs)
    v3 = choice(verbs)
    # Make sure verbs are unique
    while v1 == v2:
        v1 = choice(nouns)
    while v3 == v1 or v3 == v2:
        v3 = choice(nouns)
    
    # Select adjectives
    a1 = choice(adjectives)
    a2 = choice(adjectives)
    a3 = choice(adjectives)
    # Make sure adjectives are unique
    while a1 == a2:
        a1 = choice(adjectives)
    while a3 == a1 or a3 == a2:
        a3 = choice(adjectives)
        
    # Select prepositions
    pr1 = choice(prepositions)
    pr2 = choice(prepositions)
    # Make sure prepositions are unique
    while pr1 == pr2:
        pr1 = choice(prepositions)
        
    # Select adverbs
    ad1 = choice(adverbs)

    # Determine an article to use
    if "aeiou".find(a1[0]) != -1:
        article = "An"
    else:
        article = "A"

    # Construct a poem
    poem = "{} {} {}\n\n".format(article, a1, n1)
    poem += "{} {} {} {} {} the {} {}\n".format(article, a1, n1, v1, pr1, a2, n2)
    poem += "{}, the {} {}\n".format(ad1, n1, v2)
    poem += "the {} {} {} a {} {}".format(n2, v3, pr2, a3, n3)
    
    return poem
