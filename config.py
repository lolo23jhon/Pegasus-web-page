def get_localhost():
    uri = str()
    try:
        with open("db-uri.txt", 'r') as f:
            uri = f.read()
    except:
        uri = "bogus//bogus@bogus:1234"
    return uri

class Config(object):
    ENV = "development"
    DEBUG = True
    SECRET_KEY = "pegasus-dev-team"  # TODO: Add safer secret key.
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SQLALCHEMY_DATABASE_URI = ""  # TODO: Add heroku uri.
    
    SQLALCHEMY_DATABASE_URI = get_localhost() if DEBUG else ""



