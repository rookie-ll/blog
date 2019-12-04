from app.extends import app_extends
from flask import Flask, render_template,current_app
from app.settings import configs
from app.views import create_blue
from app.errors_header import error_header


def create_app(config_name):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(configs.get(config_name))

    #configs.get(config_name).init_app(app)

    # 初始化第三方插件
    app_extends(app)

    # 初始化蓝图
    create_blue(app)

    # 定义错误
    error_header(app)

    return app
