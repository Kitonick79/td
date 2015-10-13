from flask import Flask
#import spdb ; spdb.start(0)

import peewee

import flask_admin as admin
from flask_admin.contrib.peewee import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'

db = peewee.SqliteDatabase('test1.sqlite', check_same_thread=False)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Resource(BaseModel):
	name = peewee.CharField()

class ResourceView(ModelView):
	column_display_pk = True
	column_filters = ('name')

if __name__ == '__main__':
    
    admin = admin.Admin(app, name='Dom gde teplo')
    admin.add_view(ResourceView(Resource))

    try:
        Resource.create_table()
        
    except:
        pass
	
    app.run(debug=True)		