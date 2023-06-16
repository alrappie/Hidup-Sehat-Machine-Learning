# Recommendation
* The recommendation model is in recommendation.py using tfidf and cosine similarity for text comparison.
* The dataset is in dataset folder.
* Main notebook is notebook.ipynb

## How the model works
Here's a explanation how the recommendation works
1. Import all the needed libraries
```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity #for find the similarity text
from sklearn.feature_extraction.text import TfidfVectorizer # find the best word in all the documents
import pandas as pd # for create dataframe
import ast # for change multiple value to array
import re # regex
from markupsafe import escape, soft_str
from nltk.corpus import stopwords # remove stopwords

# get Indonesian stopword 
list_stopwords = set(stopwords.words('indonesian'))
```
2. create a class recommendation
```python
class Recommendation(): # the class's name
  
    def __init__(self,dataframe,user_input): # create a init instances
        self.tfidfvec = TfidfVectorizer() # create tfidf instances
        self.dataframe = self.prepare_dataframe(dataframe) # add to dataframe
        self.user_input = user_input # create user_input instances
      
    def prepare_dataframe(self,dataframe): # create the dataframe function
        self.dataframe = pd.read_json(dataframe,orient='records') # read the dataframe from json
        self.dataframe['cosim'] = 0
        self.dataframe['tags'] = self.dataframe['tags'].apply(lambda x: ' '.join(ast.literal_eval(x)))
        self.dataframe['text'] = self.dataframe['title']+' '+self.dataframe['summary']+' '+self.dataframe['content'] + ' ' + self.dataframe['tags'] # merge all the text
        self.dataframe['text'] = self.dataframe['text'].apply(lambda x: self.clean_text(x)) #clean the text using clean_text function
        return self.dataframe
    
    def clean_text(self,text): # create the clean_text function
        self.text = text.lower() # lower the sentences
        self.text = self.text.strip() # remove space in the beginning and the end of sentences
        self.text = re.sub('[^a-z ]','',self.text) # remove all the word except alphabet 
        self.text = ' '.join([word for word in self.text.split(' ') if not word in list_stopwords]) # remove the stopwords
        self.text = self.text.strip() # remove space
        return self.text
    
    def recomendations(self):
        self.vector = self.tfidfvec.fit_transform(self.dataframe['text']).toarray() # create vector instances from dataframe.text
        self.user_input = self.clean_text(self.user_input) # clean the user input text
        self.vector_user = self.tfidfvec.transform([self.user_input]).toarray() # create instances for vector
        self.cos_sim = cosine_similarity(self.vector,self.vector_user) # check for the similarity of the text for each documents
        self.dataframe['cosim'] = self.cos_sim
        if np.max(self.dataframe['cosim'])<=0.001: # give a recommendation based on the similarity
            return self.dataframe.sample(self.dataframe.shape[0]).drop(['text','cosim'],axis=1)
        return self.dataframe.sort_values('cosim',ascending=False).drop(['text','cosim'],axis=1)
``` 


## How to run the model
Here's a step-by-step command for run the model.
1. Clone the github
2. Import the library
```python
from recommendation import Recommendation
```
3. Run the Model with user input
```python
from recommendation import Recommendation
person = Recommendation(DATASET_LOCATION.json,USER_INPUT)
person.recomendations()
```

* Example output if user input "saya ingin menjaga kesehatan mental saya lebih baik lagi"

![images](sample_recommendation.png)
