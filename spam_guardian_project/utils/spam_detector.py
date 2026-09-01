import pickle

try:
    model = pickle.load(open('spam_model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
except:
    model, vectorizer = None, None

def predict_spam(text):
    if not model or not vectorizer:
        return 0
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
