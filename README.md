# Build a Community Board with Flask and MongoDB (with a little help from PyMongo)

1. [Teacher Notes](#teacher-notes)
2. [Demo](#demo)
3. [Want To Run This Code Yourself?](#want-to-run-this-code-yourself)
4. [How'd You Make That?](#howd-you-make-that)

## Teacher Notes

Notes for this build are located here:
- [Day 1: Introduction to MongoDB](https://github.com/upperlinecode/Upperline-Content-Master-Repo/blob/master/python-teacher-guide/lecture-guides/day-9-databases-intro.md)
- [Day 2: MongoDB Extensions](https://github.com/upperlinecode/Upperline-Content-Master-Repo/blob/master/python-teacher-guide/lecture-guides/day-10-databases-advanced.md)

## Demo

Just want to see a demo? [Click here](https://upperline-community-board.herokuapp.com/)

> If you're going to show this in a class, be sure to test the link beforehand. It may take Heroku a moment to spin up the server.

## Want To Run This Code Yourself?

If you've come just looking to run the demo code, this is a list of the packages you'll want to make sure you've installed. If you're using your own development environment, these should work as written.

> In [ide.cs50.io](https://ide.cs50.io), you may need to add a `--user` flag at the end of each: `pip install <package> --user`. 

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

And you'll need to export these variables in the Terminal:

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

- [Day 1: Introduction to MongoDB](https://github.com/upperlinecode/Upperline-Content-Master-Repo/blob/master/python-teacher-guide/lecture-guides/day-9-databases-intro.md)
- [Day 2: MongoDB Extensions](https://github.com/upperlinecode/Upperline-Content-Master-Repo/blob/master/python-teacher-guide/lecture-guides/day-10-databases-advanced.md)
