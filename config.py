import os
basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('MICROBLOG_SECRET_KEY')


OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'}]


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# added TRACK_MODIFICATIONS = false here to disable warning in pycharm
SQLALCHEMY_TRACK_MODIFICATIONS = False
WHOOSH_BASE = os.path.join(basedir, 'search.db')



# # mail server settings
# MAIL_SERVER = 'localhost'
# MAIL_PORT = 25
# MAIL_USERNAME = None
# MAIL_PASSWORD = None

# mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['stephanie.spears11@gmail.com', 'stephanie.spears11@yahoo.com']

# , 'stephanie.spears1@yahoo.com', 'stephanie.spears1@gmail.com', 'stephanie.spears11@gmail.com'


# pagination
POSTS_PER_PAGE = 10
MAX_SEARCH_RESULTS = 50
