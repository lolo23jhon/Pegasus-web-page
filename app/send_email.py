from flask_mail import Mail, Message
from . import app, mail


# TODO: set MAX_EMAIL flag in config.py.
def send_email(subject,recipients,text_body,html_body=None,cc=None,bcc=None):
    try:
        msg = Message(
            subject=subject,
            sender=app.config["MAIL_USERNAME"],
            recipients=recipients,
            cc=cc,
            bcc=bcc,
            body=text_body,
            html=html_body 
            )
        mail.send(msg)
        return "200"    
    except Exception, e:
        return str(e)