from playhouse.migrate import *
import peewee

db = peewee.SqliteDatabase('test.sqlite', check_same_thread=False)
migrator = SqliteMigrator(db)



migrate(
    # Make `notes` allow NULL values.
    migrator.drop_not_null('People', "notes"),
    migrator.rename_column('Location', 'number', 'adress')

)
