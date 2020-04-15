from get_local_host import get_local_host

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "pegasus-dev-team"
    SECURITY_PASSWORD_SALT = "Den Minecraft ist kaputt!"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_local_host()
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = True
    MAIL_USERNAME = "pegasus.csn@gmail.com"
    MAIL_DEFAULT_SENDER = "pegasus.csn@gmail.com"
    MAIL_PASSWORD = "std::cout<<\"HelloWorld!\"<<std::endl;"

    
    
    # Pagination
    APP_POSTS_PER_PAGE = 20
    APP_FOLLOWERS_PER_PAGE = 20
    APP_COMMENTS_PER_PAGE = 20

    APP_ADMINISTRATORS = ["psebastian01@gmail.com", "javierlizarraga.b@hotmail.com", "A01251527@itesm.mx"]
    APP_MODERATORS = []



