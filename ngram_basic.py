#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
# NLTK imports
import re
import unicodedata
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords

#Function for stripping stopwords, lemmatizing, removing punctuation.
def basic_clean(text):
  """
  Cleans the text data by removing stopwords, lemmatizing after encoding,
  punctuation removed with regex parsing. Returns a list of words.
  """
  wnl = nltk.stem.WordNetLemmatizer()
  stopwords = nltk.corpus.stopwords.words('english')
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words if word not in stopwords]

# LOAD THE TEXT DATA HERE as list or dataframe series
# Path to file:

# Read into df:

#Pass the text data to basic_clean in str format:
words = basic_clean(''.join(str(text_data)))

# Create a pandas series for unigrams, bigrams, etc.
# Unigrams
unigrams = (pd.Series(nltk.ngrams(words, 1)).value_counts())[:40]
# Bigrams
bigrams = (pd.Series(nltk.ngrams(words, 2)).value_counts())[:20]
# Trigrams
trigrams = (pd.Series(nltk.ngrams(words, 3)).value_counts())[:20]

# Visualise ngram
bigrams.sort_values().plot.barh(color='blue', width=.9, figsize=(12, 8))
plt.title('20 Most Frequently Occuring Bigrams')
plt.ylabel('Bigram')
plt.xlabel('# of Occurences')

# OUTPUT to Excel
# Save dataframes to separate sheets in an Excel workbook.
with pd.ExcelWriter('dipstick_out.xlsx') as writer:
  bigrams.to_excel(writer, sheet_name='Top bigrams')
  trigrams.to_excel(writer, sheet_name='Top trigrams')

# END   
