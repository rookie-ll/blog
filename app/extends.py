from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
mail = Mail()
login_manager = LoginManager()


def app_extends(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    # 用户保护级别
    # None 不开启
    # basic 默认
    # strong 开启
    login_manager.session_protection = 'strong'
    # 设置登陆拦截
    login_manager.login_view = 'user.login'
    # 设置提示信息
    login_manager.login_message = '需要登陆才能访问'


