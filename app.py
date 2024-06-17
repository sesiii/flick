import MySQLdb
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import random, string
from flask import Flask, jsonify, render_template
from flask_login import current_user, login_required
from flask import flash, redirect, render_template, request, url_for
# from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dadi:root@localhost/flick'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username_changed = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(255), unique=True, nullable=False)

import random

# Assuming you have a file 'adjectives.txt' with one adjective per line
with open('adjectives.txt') as f:
    adjectives = [line.strip() for line in f.readlines()]

animals = [

    "Penguin", "Koala", "Raccoon", "Sloth", "Unicorn", "Aardvark", "Albatross", "Alligator", "Alpaca", "Antelope",

    "Armadillo", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Blackbird", "Boa", "Boar",

    "Buffalo", "Butterfly", "Camel", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cheetah", "Chimpanzee", "Chinchilla",

    "Cobra", "Cockatoo", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Deer", "Dingo", "Dolphin", "Donkey",

    "Dragonfly", "Duck", "Eagle", "Eel", "Elephant", "Emu", "Falcon", "Ferret", "Finch", "Flamingo", "Fox", "Frog",

    "Gazelle", "Gecko", "Giraffe", "Goat", "Goose", "Gorilla", "Grasshopper", "Guinea Pig", "Hamster", "Hare", "Hawk",

    "Hedgehog", "Heron", "Hippopotamus", "Hornet", "Horse", "Hummingbird", "Hyena", "Ibex", "Ibis", "Iguana", "Jackal",

    "Jaguar", "Jellyfish", "Kangaroo", "Kingfisher", "Kiwi", "Komodo Dragon", "Lemur", "Leopard", "Llama", "Lobster",

    "Lynx", "Macaw", "Magpie", "Manatee", "Mandrill", "Meerkat", "Mole", "Mongoose", "Monkey", "Moose", "Mosquito",

    "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Orangutan", "Ostrich", "Otter", "Owl", "Ox",

    "Panda", "Panther", "Parrot", "Peacock", "Pelican", "Pheasant", "Platypus", "Porcupine", "Possum", "Prairie Dog",

    "Pufferfish", "Puma", "Quail", "Quokka", "Rabbit", "Rattlesnake", "Reindeer", "Rhino", "Robin", "Salamander",

    "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Skunk", "Snail", "Snake", "Sparrow", "Spider", "Squirrel",

    "Starfish", "Stork", "Swan", "Tapir", "Tarantula", "Tasmanian Devil", "Termite", "Tiger", "Toad", "Toucan", "Turtle",

    "Viper", "Vulture", "Wallaby", "Walrus", "Warthog", "Wasp", "Weasel", "Whale", "Wildcat", "Wolf", "Wolverine",

    "Wombat", "Woodpecker", "Worm", "Yak", "Zebra", "Zebu"

]


modifiers = [
    lambda x: x + 'o',

    lambda x: x + '-' + x,
    lambda x: x,
]
def generate_cartoon_name():
    adjective = random.choice(adjectives)
    animal = random.choice(animals)
    modifier = random.choice(modifiers)
    
    name = f"{modifier(adjective)} {animal}"
    return name

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# def generate_username():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = generate_cartoon_name()
        user = User(name=form.name.data, phone=form.phone.data, password=form.password.data, username=username)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Your username is: ' + username, 'success')
        return redirect(url_for('login'))
    return render_template('register_user.html', title='Register', form=form)

@app.route("/login_user", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('user_dashboard'))
        else:
            flash('Login Unsuccessful. Please check phone and password', 'danger')
    return render_template('login_user.html', title='Login', form=form)

from flask import render_template
from flask_login import login_required, current_user
import requests

def get_random_image_url():
    response = requests.get("https://picsum.photos/200")  # This returns a random image of 200x200 pixels
    return response.url

@app.route('/user_dashboard')
@login_required
def user_dashboard():
    # Assuming 'username', 'phone', and 'profile_photo' are attributes of your user model
    username = current_user.username
    phone = current_user.phone
    # profile_photo = get_random_image_url()
    return render_template('user_dashboard.html', username=username, phone=phone)


@app.route("/change_username", methods=['GET', 'POST'])
@login_required
def change_username():
    if current_user.username_changed:
        flash('You can only change your username once.', 'danger')
        return redirect(url_for('user_dashboard'))
    
    if request.method == 'POST':
        new_username = request.form['new_username']
        # Update the user's username in the database
        current_user.username = new_username
        current_user.username_changed = True
        db.session.commit()
        flash('Your username has been updated!', 'success')
        return redirect(url_for('user_dashboard'))
    
    return render_template('change_username.html')

@app.route("/update_user", methods=['GET', 'POST'])
@login_required
def update_user():
    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_phone = request.form.get('new_phone')
        new_password = request.form.get('new_password')

        # Update the username if it has not been changed before and a new username is provided
        if not current_user.username_changed and new_username:
            current_user.username = new_username
            current_user.username_changed = True
            flash('Your username has been updated!', 'success')

        # Update the phone number if a new phone number is provided
        if new_phone:
            current_user.phone = new_phone
            flash('Your phone number has been updated!', 'success')

        # Update the password if a new password is provided
        if new_password:
            current_user.password = new_password
            flash('Your password has been updated!', 'success')

        db.session.commit()
        return redirect(url_for('user_dashboard'))

    return render_template('update_user.html')
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)