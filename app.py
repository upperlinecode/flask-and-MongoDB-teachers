# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, request, redirect, url_for, session # added url_for, session
import bcrypt # added for password encryption
from datetime import datetime # added for date formatting
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

# set some random secret key for session
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['MONGO_DBNAME'] = 'community-board' # name of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:6zCs4vJtrzwkLBqL@cluster0-ya1yr.mongodb.net/community-board?retryWrites=true' # Command Line Tools, Connect Instructions, Secure Database (Whitelist IP), connection method (Connect Your Application) > Copy > replace password w/ password
# same for node.js > 3.0 and Python > 3.6

mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.events
    events = collection.find({})

    message = ''
    if 'username' in session:
        message = 'You are logged in as ' + session['username'] + '.'

    return render_template('events.html', events = events, message = message)



# CONNECT TO DB

@app.route('/add')

def add():
    user = mongo.db.users
    user.insert({'name':'Your Name'})
    return 'Added User!'

# Check collection for new user(s)

# NEW EVENT

@app.route('/events/new', methods=['GET', 'POST'])

def new_event():
    if request.method == "GET":
        return render_template('new_event.html')
    else:
        user_name = request.form['user_name']
        event_name = request.form['event_name']
        event_date = request.form['event_date']

        # reformat date
        dateObj = datetime.strptime(event_date, '%Y-%m-%d')
        dateStr = dateObj.strftime('%a, %b %d, %Y')

        events = mongo.db.events
        events.insert({'event': event_name, 'date': event_date, 'user': user_name, 'dateStr': dateStr})
        return redirect('/')


# EVENT PAGE (INDIVIDUAL POST)

@app.route('/events/<eventID>')

def event(eventID):
    collection = mongo.db.events
    event = collection.find_one({'_id' : ObjectId(eventID)})

    return render_template('event.html', event = event)


# DELETE EVENT

@app.route('/events/delete/<eventID>')

def delete(eventID):
    collection = mongo.db.events
    event = collection.find_one_and_delete({'_id' : ObjectId(eventID)})

    return redirect('/')


# NEW USER SIGN UP

@app.route('/signup', methods=['POST', 'GET'])

def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : str(hashpass, 'utf-8')})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists! Try logging in.'

    return render_template('signup.html')

# can clear session cookie in Developer Tools

# EXISTING USER LOGIN

@app.route('/login', methods=['POST'])

def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw((request.form['password']).encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


# USER LOGOUT

@app.route('/logout')

def logout():
    session.clear()
    return redirect('/')


# USER'S EVENTS (GATED PAGE)

@app.route('/events/myevents')

def myevents():
    collection = mongo.db.events
    username = session['username']
    events = collection.find({'user' : username})

    return render_template('my_events.html', events = events)
