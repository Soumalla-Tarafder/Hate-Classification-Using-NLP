# -*- coding: utf-8 -*-
"""Hate Classification experiment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eWfkc6Jor8tKO-4I30INt_8VKw0cepl5
"""

!nvidia-smi

!unzip /content/dataset.zip

import pandas as pd

imbalancedf = pd.read_csv("/content/imbalanced_data.csv")

imbalancedf.head()

imbalancedf.drop('id',axis = 1,inplace = True)

"""## **EDA**"""

import seaborn as sns

sns.countplot(x='label',data=imbalancedf)

"""- 0-> hate
- 1-> No Hate
"""

imbalancedf.isnull().sum()

balancedf = pd.read_csv('/content/raw_data.csv')

balancedf.head()

balancedf.isnull().sum()

balancedf = balancedf[['class','tweet']]

balancedf.head()

balancedf['class'].unique()

sns.countplot(x='class',data=balancedf)

"""- 0-> hate
- 1->abusive
- 2-> No Hate
"""

# Copy all the values of class 1 into class 0.
balancedf[balancedf['class']== 0]['class']=1

sns.countplot(x='class',data=balancedf)

balancedf['class'].replace({0:1},inplace = True)

balancedf['class'].unique()

sns.countplot(x='class',data=balancedf)

balancedf['class'].replace({2:0},inplace = True)

sns.countplot(x='class',data=balancedf)

imbalancedf.head()

balancedf.rename(columns={'class':'label'},inplace = True)

balancedf
balancedf.shape

final_Df = [balancedf,imbalancedf]
final_Df = pd.concat(final_Df)

final_Df.shape

sns.countplot(x='label',data=final_Df)

"""## Preprocessing"""

import nltk,re

from nltk.corpus import stopwords
nltk.download('stopwords')

stemmer = nltk.SnowballStemmer("english")

stopword = set(stopwords.words('english'))

stopword

import string

def data_cleaning(words):
    words = str(words).lower()
    words = re.sub('\[.*?\]', '', words)
    words = re.sub('https?://\S+|www\.\S+', '', words)
    words = re.sub('<.*?>+', '', words)
    words = re.sub('[%s]' % re.escape(string.punctuation), '', words)
    words = re.sub('\n', '', words)
    words = re.sub('\w*\d\w*', '', words)
    words = [word for word in words.split(' ') if words not in stopword]
    words=" ".join(words)
    words = [stemmer.stem(words) for word in words.split(' ')]
    words=" ".join(words)

    return words

final_Df["tweet"][1]

# let's apply the data_cleaning on the data.
final_Df['tweet']=final_Df['tweet'].apply(data_cleaning)

final_Df["tweet"][1]

x = final_Df['tweet']
y = final_Df['label']

from sklearn.model_selection import train_test_split

# Let's split the data into train and test
x_train,x_test,y_train,y_test = train_test_split(x,y, random_state = 42)

print(len(x_train),len(y_train))
print(len(x_test),len(y_test))

"""## Feature Engineering"""

from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

max_words = 50000
max_len = 300

tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(x_train)

sequences = tokenizer.texts_to_sequences(x_train)
sequences_matrix = pad_sequences(sequences,maxlen=max_len)

sequences_matrix

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding, SpatialDropout1D
from keras.optimizers import RMSprop

# Creating model architecture.
model = Sequential()
model.add(Embedding(max_words,100,input_length=max_len))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(1,activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])

# starting model training
history = model.fit(sequences_matrix,y_train,batch_size=128,epochs = 3,validation_split=0.2)

test_sequences = tokenizer.texts_to_sequences(x_test)
test_sequences_matrix = pad_sequences(test_sequences,maxlen=max_len)

test_sequences_matrix

# Model evaluation
accr = model.evaluate(test_sequences_matrix,y_test)

lstm_prediction = model.predict(test_sequences_matrix)

res = []
for prediction in lstm_prediction:
    if prediction[0] < 0.5:
        res.append(0)
    else:
        res.append(1)

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test,res))

import pickle
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Let's save the mdoel.
model.save("model.h5")

import keras

load_model=keras.models.load_model(r"/content/model.h5")
with open('/content/tokenizer.pickle', 'rb') as handle:
    load_tokenizer = pickle.load(handle)

# Let's test our model on custom data.
test = 'i love this movie'
test2 = 'you are a bitch'
def clean_text(text):
    print(text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    print(text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text

test=[clean_text(test)]
print(test)

seq = load_tokenizer.texts_to_sequences(test)
padded = pad_sequences(seq, maxlen=300)
print(seq)

pred = load_model.predict(padded)

print("pred", pred)
if pred<0.5:
    print("no hate")
else:
    print("hate and abusive")

