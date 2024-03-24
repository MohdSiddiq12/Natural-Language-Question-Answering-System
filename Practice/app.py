from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLALchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLALchemy(app)

class Todo(db.model):
   id = db.column(db.integer, primary_key = True)
   content = db.column(db.string(200), nullable=False)
   completed = db.column(db.integer, default=0)
   db.created = db.column(db.DateTime, default= datetime.utcnow)

   def __repr__(self):
      return '<Task %r>' % self.id

 
@app.route('/')
def hello_world():
   return render_template('index.html')

if __name__ == '__main__':
   app.run()