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
from datetime import datetime

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
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    online_status = db.Column(db.Boolean, default=False)
    last_location = db.Column(db.String(255))

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

@app.route('/update_location', methods=['POST'])
@login_required
def update_location():
    # Get location data from the request
    location = request.json.get('location')
    if location:
        # Update the current user's last location
        current_user.last_location = location
        db.session.commit()
        return jsonify({"success": True, "message": "Location updated successfully."})
    else:
        return jsonify({"success": False, "message": "Location not provided."}), 400
    
import math

# Define the filter function
def distance_format(value):
    """Format the distance to two decimal places and append 'km'."""
    return f"{value:.2f} km"

# Register the filter with the app's Jinja2 environment
app.jinja_env.filters['distance_format'] = distance_format

def get_nearby_users(current_user, max_distance_km):
    nearby_users = []
    for user in User.query.all():  # Assuming User is your user model
        distance = haversine(current_user.lat, current_user.lon, user.lat, user.lon)
        if distance <= max_distance_km:
            nearby_users.append((user, distance))
    return nearby_users

def haversine(lat1, lon1, lat2, lon2):
    # Earth radius in kilometers
    R = 6371.0

    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

from flask import session
from datetime import datetime, timedelta
from flask_login import current_user

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

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

from sqlalchemy import func

def get_online_users():
    # Assuming User is your user model and online_status is a boolean attribute
    online_users = User.query.filter_by(online_status=True).all()
    return online_users

@app.route("/update_user", methods=['GET', 'POST'])
@login_required
def update_user():
    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_phone = request.form.get('new_phone')
        new_password = request.form.get('new_password')
        online_status = 'online_status' in request.form  # Checks if online_status checkbox is checked

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

        # Update online status
        current_user.online_status = online_status
        flash('Your online status has been updated!', 'success')

        db.session.commit()
        return redirect(url_for('user_dashboard'))

    return render_template('update_user.html', online_status=current_user.online_status)

@app.route('/online_users')
@login_required
def online_users():
    # Assuming get_online_users is defined somewhere in this file or imported
    users = get_online_users()
    return render_template('online_users.html', users=users, get_online_users=get_online_users)

@app.route('/nearby_users')
@login_required
def nearby_users():
    # Check if current user's last_location is not None and split, else set to None
    if current_user.last_location:
        current_user_lat, current_user_lon = map(float, current_user.last_location.split(','))
    else:
        flash('Your location is not set. Please update your location to find nearby users.', 'error')
        return redirect(url_for('update_location'))  # Assuming there's a route to update location

    # Fetch all users except the current user
    users = User.query.filter(User.id != current_user.id).all()
    users_with_distance = []

    for user in users:
        if user.last_location:  # Ensure user has a location set
            try:
                user_lat, user_lon = map(float, user.last_location.split(','))
                distance = haversine(current_user_lat, current_user_lon, user_lat, user_lon)
                users_with_distance.append((user, distance))
            except ValueError:
                # Log error or pass if user's location is improperly formatted
                pass

    # Sort users by distance
    sorted_users_with_distance = sorted(users_with_distance, key=lambda x: x[1])

    return render_template('nearby_users.html', users_with_distance=sorted_users_with_distance)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)