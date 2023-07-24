from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

db = SQLAlchemy(app)



class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    

@app.route("/")
@app.route("/index")
def home():

    return render_template('index.html')


@app.route('/posts')
def posts():
    # Take from data_baze
    posts = Post.query.all()
    #########################
    return render_template('posts.html', posts=posts)


@app.route('/create', methods=['POST', "GET"])
def create():

    if request.method == 'POST':

        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

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
    app.run()