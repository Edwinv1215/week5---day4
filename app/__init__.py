from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
# from app.blueprints.main import main
# from app.blueprints.auth import auth


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)

login_manager.login_view = 'auth.login'
login_manager.login_message = 'please login first!'
login_manager.login_message_category = 'danger'


from app.blueprints.auth import auth
from app.blueprints.main import main


app.register_blueprint(auth)
app.register_blueprint(main)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

