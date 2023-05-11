# NLTK imports
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
nltk.download('punkt')
from nltk.tag import pos_tag
nltk.download('stopwords')

# spaCy imports
import spacy
from spacy.tokenizer import Tokenizer
nlp_spacy =spacy.load("en_core_web_sm")

# Other imports
import pandas as pd
import re

## Text cleaning
def remove_underscores(text:str)->str:
    return text.replace("_", " ")

# A function to remove excess whitespaces from the text
def remove_excess_whitespace(text:str)->str:
    return " ".join(text.split())

# A function to remove \n or \t from the text
def remove_newline_tab(text:str)->str:
    return text.replace("\n", " ").replace("\t", " ")

# A function to remove quotations from the text
def remove_quotations(text:str)->str:
    return re.sub(re.compile("\[\d*\]"), "", text)

# A function to clean the text by calling the above functions
def clean_text(text:str)->str:
    text = remove_underscores(text)
    text = remove_newline_tab(text)
    text = remove_quotations(text)
    text = remove_excess_whitespace(text)
    text = text.lower()
    return text


def get_filtered_tokens_set_NLTK(tokens_set):
  """A function that returns a set of unique tokens from which we have removed NLTK stopwords and punctuation"""

  stop_words =set(stopwords.words('english'))
  filtered = set()

# Remove the stop words and punctuation from the tokens set
  for token in tokens_set:
      if token not in stop_words and not token.ispunct():
          filtered.add(token)
          
  return filtered

def get_filtered_tokens_set_spacy(tokens_set):
    """A function that returns a set of unique token recognized by Spacy and then remove the stop word and punctuation """
  
    filtered = set()
    stop_word_spacy = nlp_spacy.Defaults.stop_words

    for token in tokens_set:
        if not token.is_punct and not token.is_stop:
            filtered.add(token)
    
    return filtered