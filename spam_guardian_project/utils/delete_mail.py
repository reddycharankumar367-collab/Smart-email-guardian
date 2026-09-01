def delete_spam(mail, email_id):
    mail.store(email_id, '+FLAGS', '\\Deleted')
    mail.expunge()
