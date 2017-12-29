import os
basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    # {'name': 'LiveJournal', 'url': 'http://<username>.livejournal.com'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'}]


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# added TRACK_MODIFICATIONS = false here to disable warning in pycharm
SQLALCHEMY_TRACK_MODIFICATIONS = False


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
# TODO: do i need to change the following two var?
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']
# ADMINS = ['stephanie.spears1@gmail.com', 'stephanie.spears11@gmail.com', 'stephanie.spears1@yahoo.com', 'jungletrippn@aol.com']
