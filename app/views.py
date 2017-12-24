from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm, EditForm
from .models import User
from datetime import datetime


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


# The oid.loginhandler tells Flask-OpenID that this is our login view function.
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    # At the top of the function body we check if g.user is set to an authenticated user, and in that case we redirect to the index page. The idea here is that if there is a logged in user already we will not do a second login on top.
    # The g global is setup by Flask as a place to store and share data during the life of a request
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # First we store the value of the remember_me boolean in the flask session, not to be confused with the db.session from Flask-SQLAlchemy. We've seen that the flask.g object stores and shares data though the life of a request. The flask.session provides a much more complex service along those lines. Once data is stored in the session object it will be available during that request and any future requests made by the same client. Data remains in the session until explicitly removed. To be able to do this, Flask keeps a different session container for each client of our application.
        session['remember_me'] = form.remember_me.data
        # The oid.try_login call in the following line is the call that triggers the user authentication through Flask-OpenID. The function takes two arguments, the openid given by the user in the web form and a list of data items that we want from the OpenID provider. Since we defined our User class to include nickname and email, those are the items we are going to ask for.
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    # we search our database for the email provided. If the email is not found we consider this a new user, so we add a new user to our database, pretty much as we have learned in the previous chapter. Note that we handle the case of a missing nickname, since some OpenID providers may not have that information.
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user is None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)