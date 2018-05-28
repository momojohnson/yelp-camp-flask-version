from flask_migrate import  MigrateCommand, Migrate
from flask_script import Manager

import os

from app import create_app, db
config_name = "development"
app = create_app(config_name)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
   
