import os

# contains application-wide configuration, and is loaded in __init__.py

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisIsASecretYouWillNeverGuess!' # TODO: Use this with wtforms
    DATABASE = 'database.db'
    UPLOAD_PATH = 'app/static/uploads'
    ALLOWED_EXTENSIONS = {} # Might use this at some point, probably don't want people to upload any file typef
    #RECAPTCHA_PUBLIC_KEY = ''
    #RECAPTCHA_PRIVATE_KEY = ''