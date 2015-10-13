from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

# Flask and Flask-SQLAlchemy initialization here
app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))

app.run()