from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

# SQLAlchemy
db = SQLAlchemy()

# Encriptar Password
bcrypt = Bcrypt()

# Migrate Database
migrate = Migrate()

# Login
login_manager = LoginManager()