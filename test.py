from flask import Flask
#import spdb ; spdb.start(0)

import peewee

import flask_admin as admin
from flask_admin.contrib.peewee import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'

db = peewee.SqliteDatabase('test.sqlite', check_same_thread=False)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class People(BaseModel):
    first_name   = peewee.CharField(max_length=64)
    middle_name  = peewee.CharField(max_length=64)
    last_name    = peewee.CharField(max_length=64)

    pspt_number  = peewee.IntegerField()
    pspt_address = peewee.CharField(max_length=120)
    pspt_issued  = peewee.CharField(max_length=120)
    pspt_misc    = peewee.CharField(max_length=120)

    is_head      = peewee.BooleanField()
    is_employee  = peewee.BooleanField()

    notes        = peewee.TextField(null=True)
    #family_member = peewee.FloatField()

class Resource(BaseModel):
    name          = peewee.CharField(max_length=120)
    description   = peewee.TextField(null=True)
    number        = peewee.IntegerField(null=True)

class Location(BaseModel):
    name          = peewee.CharField(max_length=64)
    description   = peewee.TextField(null = True)
    adress        = peewee.IntegerField(null= True)



class PeopleView(ModelView):

    #Visible columns in the list view
    column_exclude_list = ('middle_name', 'pspt_misc', 'pspt_issued',  'pspt_address', 'pspt_number')

    # List of columns that can be sorted.
    column_sortable_list = ('last_name', 'is_head')

    # Column filters
    column_filters = ('last_name',
                      'is_head',
                      'is_employee'
                      )    
    column_display_pk = 'True'

class ResourceView(ModelView):
    column_filters = ('name', )
    column_display_pk = 'True'

class LocationView(ModelView):
    #column_filters = ( 'name' )
    column_display_pk = 'True'



@app.route('/')
def index():
   return '<a href="/admin/">Click me to get to Admin!</a>'
   #return render_template('index.html')


if __name__ == '__main__':
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    admin = admin.Admin(app, name='Dom gde teplo')
    admin.add_view(PeopleView(People))
    admin.add_view(ResourceView(Resource))
    admin.add_view(LocationView(Location))
    #admin.add_view(UserAdmin(User))
    #admin.add_view(PostAdmin(Post))

    try:
        People.create_table()
        Resource.create_table()
        Location.create_table()
        
    except:
        pass

    app.run(debug=True)