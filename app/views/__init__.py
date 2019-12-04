from .main import main
from .user import user



def create_blue(app):
    app.register_blueprint(main)
    app.register_blueprint(user)


# url_prefix
from . import main
from . import user
