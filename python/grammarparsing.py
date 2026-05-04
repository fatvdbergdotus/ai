# Import required libraries
import nltk
from nltk import CFG
from nltk.parse import ChartParser

'''
In grammar parsing, symbols like S, NP, VP, and PP represent different parts of a sentence structure: S (Sentence) is the complete sentence, 
usually made up of a noun phrase (NP) and a verb phrase (VP); NP refers to a group of words acting as a noun (like “the big dog”), while VP 
contains the verb and its object or action (like “saw a cat”); PP (prepositional phrase) adds extra information such as location or manner 
(like “with a telescope”). Other components include Det (determiner) like “the” or “a,” N (noun) like “dog,” V (verb) like “saw,” Adj (adjective) 
like “big,” and P (preposition) like “with,” all working together to define how sentences are grammatically structured.
'''

# ----------------------------------------
# 1. Define grammar (rules of the language)
# ----------------------------------------
# CFG = Context-Free Grammar
# This defines how sentences can be structured
grammar = CFG.fromstring("""
S -> NP VP              

NP -> Det N             
NP -> Det Adj N         
NP -> NP PP             

VP -> V NP              
VP -> VP PP             

PP -> P NP              

Det -> 'the' | 'a'      
Adj -> 'big'            
N -> 'dog' | 'cat' | 'telescope'  
V -> 'saw'              
P -> 'with'             
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

'''
OUTPUT:

  (VP
    (V saw)
    (NP
      (NP (Det a) (N cat))
      (PP (P with) (NP (Det a) (N telescope))))))
                 S                                
      ___________|_______                          
     |                   VP                       
     |        ___________|___                      
     |       |               NP                   
     |       |        _______|____                 
     |       |       |            PP              
     |       |       |        ____|___             
     NP      |       NP      |        NP          
  ___|___    |    ___|___    |     ___|______      
Det Adj  N   V  Det      N   P   Det         N    
 |   |   |   |   |       |   |    |          |     
the big dog saw  a      cat with  a      telescope

'''
