from flask import Flask, render_template, request, redirect, session
import pg
import traceback

db = pg.DB(dbname='github_db')

app = Flask('MyApp')

@app.route('/')
def home():

    return render_template(
        'login.html',
        title='Sign In'
    )

@app.route('/form')
def forms():
    return render_template(
        'form.html',
        title='Add A Project'
    )

@app.route('/login', methods=['POST'])
def login():
    try:
        signin_name = request.form['coder_name']
        session['signin_name'] = signin_name
        query_string ="select coder.name as name from coder where coder.name = '%s'" % signin_name

        name = db.query(query_string)

        if signin_name == name.namedresult()[0].name:
            return redirect('/form')
        else:
            return redirect('/')
    except Exception, e:
        print traceback.format_exc()
        return "Error %s" % traceback.format_exc()


@app.route('/submit', methods=['POST'])
def submits():
    project_name = request.form['project_name']
    project_stars = request.form['project_stars']
    project_date = request.form['project_date']
    db.insert('project', name=project_name, stars=project_stars, date=project_date)
    return redirect('/form')

app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'


if __name__ == '__main__':
    app.run(debug=True)
