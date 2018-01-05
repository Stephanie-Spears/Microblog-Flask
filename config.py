import os
basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('MICROBLOG_SECRET_KEY')


OPENID_PROVIDERS = [
    # NOTE: as of 2018 only Yahoo and AOL still provide OpenID support
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')


# pagination
POSTS_PER_PAGE = 4
MAX_SEARCH_RESULTS = 50


# NOTE (WE ARE USING POP):
#     IMAP (Internet Message Access Protocol) is a newer protocol that allows you to remotely access and manage your email. What you do in the app affects email on the email server.
#     POP (Post Office Protocol) is an older protocol that copies emails from the email server to the app. Actions performed in the app don't affect email on the email server.


# # GMAIL mail server settings FOR OUTGOING SSL --> #from google to google works, from google to yahoo works --> must enable less secure apps in gmail to allow mail to be sent
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = os.environ.get('GMAIL_USERNAME_ONE_ONE')
# MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD_ONE_ONE')

# # YAHOO mail OUTGOING server settings ->
# Must set mail server (ADMIN[0]) to allow less secure apps
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('YMAIL_USERNAME_ONE_ONE')
MAIL_PASSWORD = os.environ.get('YMAIL_PASSWORD_ONE_ONE')

# administrator list # SENDER = ADMINS[0], RECIPIENTS = ADMINS (both)
ADMINS = ['stephanie.spears11@yahoo.com', 'stephanie.spears11@gmail.com']


# added TRACK_MODIFICATIONS = false here to disable warning in pycharm
SQLALCHEMY_TRACK_MODIFICATIONS = False