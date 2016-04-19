from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        <p>"Hi! This is the home page."<p>
        <a href="http://localhost:5000/hello">Click here to get started.</a>
      </body>
    </html>
    """
    


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit">
          <select name="compliment">
            <option value="a great listener!">a great listener!</option>
            <option value="intelligent!">intelligent!</option>
            <option value="smokin' hot!">smokin' hot!</option>
          </select>
        </form>
      </body>
    </html>
    """
        # <form action="/diss">
        #   <select name="diss">
        #     <option value="acting like a child!">acting like a child!</option>
        #     <option value="a terrible programmer!">a terrible programmer!</option>
        #     <option value="not that bad!">not that bad!</option>
        # </form>

@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s, I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

# @app.route('/diss')
# def diss_person():
#   """Get user by name, allows user to select a diss, and returns to user."""
#     player = request.args.get("person")

#     diss = request.args.get("diss")


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
