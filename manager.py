from app import create_app
import os
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app(config_name=os.environ.get("FLASK_CONFIG", "development"))
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
