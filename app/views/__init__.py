from .main import main
from .user import user
from .post import post_blue


def create_blue(app):
    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(post_blue)


# url_prefix
from . import main
from . import user
from . import post
