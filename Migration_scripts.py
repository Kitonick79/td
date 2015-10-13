from playhouse.migrate import *
import peewee

db = peewee.SqliteDatabase('test.sqlite', check_same_thread=False)
migrator = SqliteMigrator(my_db)

migrate(
    # Make `notes` allow NULL values.
    migrator.drop_not_null('notes',  'pspt_number', 'pspt_address', 'pspt_issued', 'pspt_misc'),

    # Prevent `modified_date` from containing NULL values.
    migrator.add_not_null(('notes',  'pspt_number', 'pspt_address', 'pspt_issued', 'pspt_misc'),
)