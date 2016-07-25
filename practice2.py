# the Flask class from the flask module
from flask import Flask, render_template
import pg

db = pg.DB(dbname='restaurant_db')

# creates a flask app object
app = Flask('MyApp')

# sets up a URL handler for the root URL:
@app.route('/')
def reviews():
    # query the database
    query = db.query('''
        select
            *
        from
            restaurant
        left outer join
            review on restaurant.id = review.restaurant_id
    ''')
    # use the template to build up HTML to be sent to the browser
    return render_template(
        'top10.html',
        title='Restaurants',
        reviews=query.namedresult())

# start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will auto-restart the server on ever save
    app.run(debug=True)
