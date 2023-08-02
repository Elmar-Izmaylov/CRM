from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    age = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    time = db.Column(db.String(255))
    day = db.Column(db.String(255))

    


@app.route('/')
def posts():
    # Take from data_baze
    posts = Post.query.all()
    #########################
    return render_template('posts.html', posts=posts)


@app.route('/create', methods=['POST', "GET"])
def create():

    if request.method == 'POST':

        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        phone = request.form['phone']
        time = request.form['time']
        day = request.form['day']

        post = Post(name=name,surname=surname, age=age, phone=phone, time=time, day=day)

        try:
            # ADD in data_base
            db.session.add(post)

            # SAVE in data_base
            db.session.commit()
            # / path(/ or index) func=home()
            return redirect('/')
        
        except:
            return "{}".format("An error occurred while adding a record to the database")

    else:
        return render_template('create.html')


if __name__ == '__main__':
    with app.app_context():
        # Inside the app_context block, you can access the database
        # and perform other operations that require the application context.
        # For example, you can create the database tables:
        db.create_all()

    # Finally, run the Flask application
    app.run(debug=True)