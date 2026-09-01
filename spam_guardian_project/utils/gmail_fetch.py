import imaplib
import email

def fetch_emails(user, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user, password)
    mail.select('inbox')

    _, data = mail.search(None, 'ALL')
    mail_ids = data[0].split()

    emails = []
    for num in mail_ids[-10:]:
        _, msg_data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        subject = msg['subject']
        emails.append((num, subject))

    return mail, emails
