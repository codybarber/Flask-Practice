# the Flask class from the flask module
from flask import Flask

# creates a flask app object
app = Flask('MyApp')

# sets up a URL handler for the root URL:
@app.route('/')
def hello():
    # send the text "Hello, World!" to the browser
    return '<h1>Hello, World!</h1>'

# start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will auto-restart the server on ever save
    app.run(debug=True)
