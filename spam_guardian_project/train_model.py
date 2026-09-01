from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

df = pd.read_csv('spam.csv', encoding='latin-1')

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['v2'])
y = df['v1'].map({'ham':0, 'spam':1})

model = MultinomialNB()
model.fit(X, y)

pickle.dump(model, open('spam_model.pkl','wb'))
pickle.dump(vectorizer, open('vectorizer.pkl','wb'))

print("Model trained and saved!")
