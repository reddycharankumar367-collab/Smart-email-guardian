from flask import Flask, render_template, request
from utils.gmail_fetch import fetch_emails
from utils.spam_detector import predict_spam
from utils.delete_mail import delete_spam

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []

    if request.method == 'POST':
        email_user = request.form['email']
        password = request.form['password']

        mail, emails = fetch_emails(email_user, password)

        for eid, subject in emails:
            if predict_spam(subject) == 1:
                delete_spam(mail, eid)
                results.append((subject, 'Deleted Spam'))
            else:
                results.append((subject, 'Safe'))

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
