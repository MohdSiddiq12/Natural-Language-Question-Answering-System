from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLALchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLALchemy(app)
 
@app.route('/')
def hello_world():
   return render_template('index.html')

if __name__ == '__main__':
   app.run()