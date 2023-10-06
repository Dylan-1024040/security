from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite://database.db"
db.init_app(app)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug=True)
    