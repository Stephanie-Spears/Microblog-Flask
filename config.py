import os
basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'Stack Exchange', 'url': 'https://openid.stackexchange.com/<username>'}]


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# TODO: added TRACK_MODIFICATIONS = false here to disable warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
