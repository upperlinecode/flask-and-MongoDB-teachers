# Build a Community Board with Flask and MongoDB (with a little help from PyMongo)

1. [Teacher Notes](#teacher-notes)
2. [Demo](#demo)
3. [Want To Run This Code Yourself?](#want-to-run-this-code-yourself)
4. [How'd You Make That?](#howd-you-make-that)

## Teacher Notes

Notes for this build are located here:
- [Day 1: Introduction to MongoDB](https://teacherhub.upperlinecode.com/day-9-databases-intro)
- [Day 2: MongoDB Extensions](https://teacherhub.upperlinecode.com/day-11-databases-advanced)

## Demo

Just want to see a demo? [Click here](https://upperline-community-board.herokuapp.com/)

> If you're going to show this in a class, be sure to test the link beforehand. It may take Heroku a moment to spin up the server.

## Want To Run This Code Yourself?

If you've come just looking to run the demo code, this is a list of the packages you'll want to make sure you've installed. If you're using your own development environment, these should work as written.

```python
pip install flask
pip install flask-pymongo # for mongodb connection
pip install dnspython # for mongodb connection
pip install bcrypt # for password handling
pip install bson # for page/post
pip install datetime # for prettifying dates
```

Or all in one:

```python
pip install flask flask-pymongo dnspython bcrypt bson datetime
```

> Depending on which code editor you use, `pip install <package>` may or may not be enough to install a package. Two additional methods you could try to ensure a package is installed are:
>
> - `sudo pip install <package>` can force the installation if a user has sufficient privileges
> - `pip install <package> --user` can do the installation just for the user's account

And you'll need to export these variables in the Terminal if they haven't already been saved during your environment setup:

```bash
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```

To view the finished app, execute `flask run` in the Terminal.

> Test out how to submit an event, sign up, log in, view an event page, and log out.
> 
> Examine `routes.py` to see how each action is implemented.

### How'd You Make That?

- [Day 1: Introduction to MongoDB](https://teacherhub.upperlinecode.com/day-9-databases-intro)
- [Day 2: MongoDB Extensions](https://teacherhub.upperlinecode.com/day-11-databases-advanced)
