# Import required libraries
import nltk
from nltk import CFG
from nltk.parse import ChartParser

# ----------------------------------------
# 1. Define grammar (rules of the language)
# ----------------------------------------
# CFG = Context-Free Grammar
# This defines how sentences can be structured
grammar = CFG.fromstring("""
S -> NP VP              # A sentence = Noun Phrase + Verb Phrase

NP -> Det N             # Noun Phrase = Determiner + Noun
NP -> Det Adj N         # Noun Phrase = Determiner + Adjective + Noun
NP -> NP PP             # Noun Phrase can be extended with a Prepositional Phrase

VP -> V NP              # Verb Phrase = Verb + Noun Phrase
VP -> VP PP             # Verb Phrase can also include a Prepositional Phrase

PP -> P NP              # Prepositional Phrase = Preposition + Noun Phrase

Det -> 'the' | 'a'      # Determiners
Adj -> 'big'            # Adjectives
N -> 'dog' | 'cat' | 'telescope'  # Nouns
V -> 'saw'              # Verb
P -> 'with'             # Preposition
""")

# ----------------------------------------
# 2. Create parser
# ----------------------------------------
# ChartParser efficiently parses sentences using dynamic programming
parser = ChartParser(grammar)

# ----------------------------------------
# 3. Input sentence
# ----------------------------------------
# Split sentence into words (tokens)
sentence = "the big dog saw a cat with a telescope".split()

# ----------------------------------------
# 4. Parse the sentence
# ----------------------------------------
# Generate all possible parse trees (because sentence is ambiguous)
trees = list(parser.parse(sentence))

# ----------------------------------------
# 5. Display results
# ----------------------------------------
for i, tree in enumerate(trees):
    print(f"\nParse Tree {i+1}:")
    
    # Print tree in text format
    print(tree)
    
    # Pretty visual tree structure
    tree.pretty_print()
